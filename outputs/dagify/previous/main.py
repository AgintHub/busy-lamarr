import os
import asyncio
import functools
import inspect
import json
import sys
from typing import Dict, Any, List, Callable, Coroutine, Union, Optional

from code.definenumericinterpretations import definenumericinterpretations
from code.definesupportedcodecs import definesupportedcodecs
from code.designcommandlineinterface import designcommandlineinterface
from code.implementbinarydatareader import implementbinarydatareader
from code.implementcodecapplication import implementcodecapplication
from code.implementnumericinterpretation import implementnumericinterpretation
from code.integratecliwithparsinglogic import integratecliwithparsinglogic
from code.testclitool import testclitool

# Get async mode from environment variable or default to False
ASYNC_MODE = os.environ.get('ASYNC_MODE', '').lower() in ('true', '1', 'yes', 'y')

def make_async(func):
    """Convert a synchronous function to an asynchronous function.

    If the function is already asynchronous, return it unchanged.
    If the function is synchronous, wrap it in an async function.
    """
    # If it's already a coroutine function, return it as is
    if inspect.iscoroutinefunction(func):
        return func

    # Otherwise, wrap it as an async function
    @functools.wraps(func)
    async def async_wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return async_wrapper

definenumericinterpretations_async = make_async(definenumericinterpretations)
definesupportedcodecs_async = make_async(definesupportedcodecs)
designcommandlineinterface_async = make_async(designcommandlineinterface)
implementbinarydatareader_async = make_async(implementbinarydatareader)
implementcodecapplication_async = make_async(implementcodecapplication)
implementnumericinterpretation_async = make_async(implementnumericinterpretation)
integratecliwithparsinglogic_async = make_async(integratecliwithparsinglogic)
testclitool_async = make_async(testclitool)

async def run_workflow(user_input: str) -> Dict[str, Any]:
    """Execute the workflow by running each level in the topological sort.

    Args:
        user_input: The input string for the workflow

    Returns:
        Dict containing all results keyed by node name
    """
    # Store results for each node
    results = {}

    # Level 0: definenumericinterpretations, implementbinarydatareader, definesupportedcodecs
    async def run_definenumericinterpretations():
        # Call the async version of definenumericinterpretations with results from dependencies
        return await definenumericinterpretations_async(user_input)

    async def run_implementbinarydatareader():
        # Call the async version of implementbinarydatareader with results from dependencies
        return await implementbinarydatareader_async(user_input)

    async def run_definesupportedcodecs():
        # Call the async version of definesupportedcodecs with results from dependencies
        return await definesupportedcodecs_async(user_input)

    # Run level 0 nodes in parallel
    level_0_results = await asyncio.gather(run_definenumericinterpretations(), run_implementbinarydatareader(), run_definesupportedcodecs())
    results['definenumericinterpretations'] = level_0_results[0]
    results['implementbinarydatareader'] = level_0_results[1]
    results['definesupportedcodecs'] = level_0_results[2]

    # Level 1: implementnumericinterpretation, implementcodecapplication, designcommandlineinterface
    async def run_implementnumericinterpretation():
        # Call the async version of implementnumericinterpretation with results from dependencies
        return await implementnumericinterpretation_async(results['definenumericinterpretations'], results['implementbinarydatareader'])

    async def run_implementcodecapplication():
        # Call the async version of implementcodecapplication with results from dependencies
        return await implementcodecapplication_async(results['definesupportedcodecs'], results['implementbinarydatareader'])

    async def run_designcommandlineinterface():
        # Call the async version of designcommandlineinterface with results from dependencies
        return await designcommandlineinterface_async(results['definesupportedcodecs'], results['definenumericinterpretations'])

    # Run level 1 nodes in parallel
    level_1_results = await asyncio.gather(run_implementnumericinterpretation(), run_implementcodecapplication(), run_designcommandlineinterface())
    results['implementnumericinterpretation'] = level_1_results[0]
    results['implementcodecapplication'] = level_1_results[1]
    results['designcommandlineinterface'] = level_1_results[2]

    # Level 2: integratecliwithparsinglogic
    async def run_integratecliwithparsinglogic():
        # Call the async version of integratecliwithparsinglogic with results from dependencies
        return await integratecliwithparsinglogic_async(results['designcommandlineinterface'], results['implementcodecapplication'], results['implementnumericinterpretation'])

    # Run level 2 nodes in parallel
    results['integratecliwithparsinglogic'] = await run_integratecliwithparsinglogic()

    # Level 3: testclitool
    async def run_testclitool():
        # Call the async version of testclitool with results from dependencies
        return await testclitool_async(results['integratecliwithparsinglogic'])

    # Run level 3 nodes in parallel
    results['testclitool'] = await run_testclitool()

    # Return all results
    return results

def run_workflow_sync(user_input: str) -> Dict[str, Any]:
    """Synchronous wrapper around the async workflow execution."""
    return asyncio.run(run_workflow(user_input))

def main():
    """Main entry point.

    Handles arguments in the following priority:
    1. Command-line argument (sys.argv[1])
    2. If no argument, uses empty string as input but displays a warning.
    """
    # Get user input from command line or use empty string
    if len(sys.argv) > 1:
        user_input = sys.argv[1]
    else:
        # No input provided - display help message but continue with empty string
        print('Warning: No input provided. Using empty string as input.')
        print('For better results, provide an input argument:')
        print(f'  python {os.path.basename(__file__)} "your input text here"')
        print('Or use a file as input:')
        print(f'  python {os.path.basename(__file__)} "$(cat input.txt)"')
        user_input = ""

    print(f'Running workflow with input: {user_input}')

    # Run the workflow
    results = run_workflow_sync(user_input)

    # Print results
    try:
        # Convert results to JSON
        json_results = json.dumps(results, indent=2, default=str)
        print(json_results)
    except (TypeError, ValueError) as e:
        print(f'Results could not be converted to JSON: {e}')
        print(f'Raw results: {results}')

    return results

if __name__ == '__main__':
    main()

import argparse
import importlib
from setup import Setup

def run_script(script_name): 

    try:
         module = importlib.import_module(f"data_processing.{script_name}")

         module.main(Setup)

    except ImportError: 
         print(
              f'Error: Module "{script_name}" not found or Python package doesnt exist.'
         )


if __name__ == "__main__": 
     
     parser = argparse.ArgumentParser()
     parser.add_argument("pipeline", nargs="*")
     args = parser.parse_args()

     for pipeline in args.pipeline: 
          print(f"Starting {pipeline} pipeline")

          run_script(pipeline)

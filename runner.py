import os
import pathlib
import subprocess
import argparse
from datetime import datetime
from pdb import set_trace


def get_unique_run_id():

    if os.environ.get("BUILD_NUMBER"):
        unique_run_id = os.environ.get("BUILD_NUMBER")
    else:
        unique_run_id = datetime.now().strftime('%Y%m%d%H%M')

    os.environ['UNIQUE_RUN_ID'] = unique_run_id

    return unique_run_id

def create_output_directory(prefix='results_'):

    global run_id
    if not run_id:
        raise Exception("Variable 'run_id' is not set. Unable to create output directory")

    curr_file_path = pathlib.Path(__file__).parent.absolute()
    dir_to_create = os.path.join(curr_file_path, prefix + str(run_id))
    os.mkdir(dir_to_create)

    print(f"Created output directory: {dir_to_create}")

    return dir_to_create

if __name__ == '__main__':

    #################### INITIAL CHECKS ####################

    # Check that the website is up and running
    import urllib.request
    from urllib.error import URLError, HTTPError
    import sys

    try:
        with urllib.request.urlopen("https://osdatahub.os.uk/", timeout=10) as response:
            if response.status == 200:
                print(f"Website: https://osdatahub.os.uk/ is up and running.")
            else:
                print(f"Website https://osdatahub.os.uk/ returned status: {response.status}")
                sys.exit(f"Exiting: Website returned status {response.status}")
    except HTTPError as e:
        print(f"HTTP error occurred: {e.code} - {e.reason}")
        sys.exit("Exiting: HTTP error")
    except URLError as e:
        print(f"Failed to reach server: {e.reason}")
        sys.exit("Exiting: URL error")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit("Exiting: Unknown error")

    #################### END CHECKS ####################

    run_id = get_unique_run_id()
    parser = argparse.ArgumentParser()
    parser.add_argument('--test_dir', required=False, help="Location of test files")
    parser.add_argument('--behave_options', type=str,required=False,
                        help="Can specify behave options such as tags to run with either -t <tag name> or "
                             "--tags=api,homepage")
    parser.add_argument('--output_html', required=False, help="Enter yes to output a html report file")

    args = parser.parse_args()
    test_dir = args.test_dir
    behave_options = '' if not args.behave_options else args.behave_options

    # Since we will be using jenkins build to trigger then we can check if the tags parameter is passed in or not
    # Remove '--tags=' string if its None or empty
    tags_jenkins_parameter = os.environ.get('tags')
    if tags_jenkins_parameter is None and os.environ.get('JENKINS_HOME') is not None:
        behave_options = behave_options.replace('--tags=', '')

    output_html = '' if not args.output_html else args.output_html
    if output_html != '':
        curr_file_path = pathlib.Path(__file__).parent.absolute()
        dir_to_report = os.path.join(curr_file_path, 'reports/')
        if not os.path.exists(dir_to_report):
            os.mkdir(dir_to_report)
        dir_to_report = dir_to_report + 'behave-report.html'
        # output_json = f'-f json.pretty -o reports/json-report.json'
        output_html = f'-f html-pretty -o {dir_to_report} '

    command = f'behave -k --no-capture {output_html}' \
              f'{behave_options} ' \
              f'{test_dir}'
    print(f'Running command: {command}')
    rs = subprocess.run(command, shell=True)







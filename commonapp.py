import multiprocessing
from contractdraft import app as contract_draft_app
from tester import app as tester_app
from viewroyalty import app as view_royalty_app

if __name__ == '__main__':
    # Create processes for each Flask application
    processes = [
        multiprocessing.Process(target=contract_draft_app.run, kwargs={'debug': True}),
        multiprocessing.Process(target=tester_app.run, kwargs={'debug': True}),
        multiprocessing.Process(target=view_royalty_app.run, kwargs={'debug': True})
    ]

    # Start all processes
    for process in processes:
        process.start()

    # Wait for all processes to finish
    for process in processes:
        process.join()

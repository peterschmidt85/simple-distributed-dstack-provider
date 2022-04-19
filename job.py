import os

if __name__ == '__main__':
    os.makedirs(f"output/{os.getenv('JOB_NUMBER')}", exist_ok=True)
    with open(f"output/{os.getenv('JOB_NUMBER')}/data.txt", "w") as f:
        f.write(os.getenv('JOB_NUMBER'))

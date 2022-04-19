from typing import List

from dstack import Provider, Job


class HelloProvider(Provider):
    def __init__(self):
        super().__init__()

    def create_jobs(self) -> List[Job]:
        job1 = Job(
            image_name="python:3.9",
            commands=["JOB_NUMBER=1 python3 job.py"],
            artifacts=["output/1"]
        )
        job2 = Job(
            image_name="python:3.9",
            commands=["JOB_NUMBER=2 python3 job.py"],
            artifacts=["output/2"]
        )
        job3 = Job(
            image_name="python:3.9",
            commands=["find output"],
            depends_on=[job1, job2]
        )
        return [
            job1,
            job2,
            job3
        ]


if __name__ == '__main__':
    HelloProvider().start()

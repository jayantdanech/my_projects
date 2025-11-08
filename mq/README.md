
### To push a task
docker exec -it python_app bash

### To send task, use below inside the docker
python producer.py


### How to check on Redis:
docker exec -it redis redis-cli

keys *

## Example:
127.0.0.1:6379> keys *
1) "celery-task-meta-638ff4a1-35fb-4ca8-ae6c-f06dc84a0772"
2) "celery-task-meta-105da142-614d-457a-a6b8-07ad83130d90"
3) "celery-task-meta-d3aa38c5-3d00-4ee9-ba4c-c5905bf4bbfe"

127.0.0.1:6379> get celery-task-meta-d3aa38c5-3d00-4ee9-ba4c-c5905bf4bbfe
"{\"status\": \"SUCCESS\", \"result\": 30, \"traceback\": null, \"children\": [], \"date_done\": \"2025-11-08T13:21:42.737182+00:00\", \"task_id\": \"d3aa38c5-3d00-4ee9-ba4c-c5905bf4bbfe\"}"

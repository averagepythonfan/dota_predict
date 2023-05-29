test:
	echo "this is test"
storage_test:
	docker compose up minio_s3 lab -d
lab_url:
	docker logs jupyter_lab 2>&1 | grep 'http' | tail -1
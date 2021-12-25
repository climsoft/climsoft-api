build:
	docker-compose build

serve:
	docker-compose up --remove-orphans --force-recreate

test:
	docker-compose -f docker-compose.test.yml run test_climsoft_api; docker-compose -f docker-compose.test.yml down

test_build:
	docker-compose -f docker-compose.test.yml build

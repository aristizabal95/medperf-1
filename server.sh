ADMIN_TOKEN=$(curl -X POST "http://127.0.0.1:8000/auth-token/" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{  \"username\": \"admin\",  \"password\": \"admin\"}" | jq -r '.token')

echo $ADMIN_TOKEN

BENCHMARK_OWNER=$(curl -X POST "http://127.0.0.1:8000/users/" -H  "accept: application/json" -H  "Authorization: Token $ADMIN_TOKEN" -H  "Content-Type: application/json" -d "{  \"username\": \"testbenchmarkowner\",  \"email\": \"testbo@example.com\",  \"password\": \"test\",  \"first_name\": \"testowner\",  \"last_name\": \"benchmark\"}" | jq -r .username)

MODEL_OWNER=$(curl -X POST "http://127.0.0.1:8000/users/" -H  "accept: application/json" -H  "Authorization: Token $ADMIN_TOKEN" -H  "Content-Type: application/json" -d "{  \"username\": \"testmodelowner\",  \"email\": \"testmo@example.com\",  \"password\": \"test\",  \"first_name\": \"testowner\",  \"last_name\": \"model\"}" | jq -r .username)

DATASET_OWNER=$(curl -X POST "http://127.0.0.1:8000/users/" -H  "accept: application/json" -H  "Authorization: Token $ADMIN_TOKEN" -H  "Content-Type: application/json" -d "{  \"username\": \"testdataowner\",  \"email\": \"testdo@example.com\",  \"password\": \"test\",  \"first_name\": \"testowner\",  \"last_name\": \"data\"}" | jq -r .username)

BENCHMARK_OWNER_TOKEN=$(curl -X POST "http://127.0.0.1:8000/auth-token/" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{  \"username\": \"$BENCHMARK_OWNER\",  \"password\": \"test\"}" | jq -r '.token')

MODEL_OWNER_TOKEN=$(curl -X POST "http://127.0.0.1:8000/auth-token/" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{  \"username\": \"$MODEL_OWNER\",  \"password\": \"test\"}" | jq -r '.token')

DATASET_OWNER_TOKEN=$(curl -X POST "http://127.0.0.1:8000/auth-token/" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{  \"username\": \"$DATASET_OWNER\",  \"password\": \"test\"}" | jq -r '.token')


DATA_PREPROCESSOR_MLCUBE=$(curl -X POST "http://127.0.0.1:8000/mlcubes/" -H  "accept: application/json" -H  "Authorization: Token $BENCHMARK_OWNER_TOKEN" -H  "Content-Type: application/json" -d "{  \"name\": \"datapreprocessor\",  \"git_url\": \"string\",  \"tarball_url\": \"string\",  \"tarball_hash\": \"string\",  \"metadata\": {},  \"status\": \"APPROVED\"}" | jq -r '.id')

REFERENCE_MODEL_EXECUTOR_MLCUBE=$(curl -X POST "http://127.0.0.1:8000/mlcubes/" -H  "accept: application/json" -H  "Authorization: Token $BENCHMARK_OWNER_TOKEN" -H  "Content-Type: application/json" -d "{  \"name\": \"reference-model\",  \"git_url\": \"string\",  \"tarball_url\": \"string\",  \"tarball_hash\": \"string\",  \"metadata\": {},  \"status\": \"APPROVED\"}" | jq -r '.id')


DATA_EVALUATOR_MLCUBE=$(curl -X POST "http://127.0.0.1:8000/mlcubes/" -H  "accept: application/json" -H  "Authorization: Token $BENCHMARK_OWNER_TOKEN" -H  "Content-Type: application/json" -d "{  \"name\": \"evaluator\",  \"git_url\": \"string\",  \"tarball_url\": \"string\",  \"tarball_hash\": \"string\",  \"metadata\": {},  \"status\": \"APPROVED\"}" | jq -r '.id')


BENCHMARK=$(curl -X POST "http://127.0.0.1:8000/benchmarks/" -H  "accept: application/json" -H  "Authorization: Token $BENCHMARK_OWNER_TOKEN" -H  "Content-Type: application/json" -d "{  \"name\": \"testbenchmark\",  \"description\": \"benchmark-sample\",  \"docs_url\": \"string\",  \"data_preparation_mlcube\": $DATA_PREPROCESSOR_MLCUBE,  \"reference_model_mlcube\": $REFERENCE_MODEL_EXECUTOR_MLCUBE,  \"data_evaluator_mlcube\": $DATA_EVALUATOR_MLCUBE}" | jq -r '.id')

MODEL_EXECUTOR1_MLCUBE=$(curl -X POST "http://127.0.0.1:8000/mlcubes/" -H  "accept: application/json" -H  "Authorization: Token $MODEL_OWNER_TOKEN" -H  "Content-Type: application/json" -d "{  \"name\": \"model-executor1\",  \"git_url\": \"string\",  \"tarball_url\": \"string\",  \"tarball_hash\": \"string\",  \"metadata\": {},  \"status\": \"APPROVED\"}" | jq -r '.id')


DATASET=$(curl -X POST "http://127.0.0.1:8000/datasets/" -H  "accept: application/json" -H  "Authorization: Token $DATASET_OWNER_TOKEN" -H  "Content-Type: application/json" -d "{  \"name\": \"dataset\",  \"description\": \"dataset-sample\",  \"location\": \"string\",  \"generated_uid\": \"string\",  \"split_seed\": 0,  \"metadata\": {},  \"status\": \"APPROVED\",  \"data_preparation_mlcube\": $DATA_PREPROCESSOR_MLCUBE}" | jq -r '.id') 

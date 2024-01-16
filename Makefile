GENERATED_DIR=generated

codegen:
	rm -rf ${GENERATED_DIR}
	openapi-generator generate \
		-i https://developer.digiseg.net/openapi.json \
		-g python -o ${GENERATED_DIR} \
		--additional-properties packageName=digiseg_api,projectName=digiseg-api-client \
		--git-user-id digiseg-labs \
		--git-repo-id api-client-python
	mv ${GENERATED_DIR}/digiseg_api .
	mv ${GENERATED_DIR}/pyproject.toml .
	mv ${GENERATED_DIR}/setup.cfg .
	mv ${GENERATED_DIR}/setup.py .
	mv ${GENERATED_DIR}/requirements.txt .

clean:
	rm -rf ${GENERATED_DIR}

.PHONY: build
build:

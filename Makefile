.PHONY: backend frontend start restart stop

backend:
	uv run uvicorn app.main:app --reload

frontend:
	uv run streamlit run frontend/app.py

start:
	@echo "Iniciando backend y frontend..."
	make -j2 backend frontend

stop:
	@echo "Deteniendo procesos en puertos 8000 y 8501..."
	-@fuser -k 8000/tcp
	-@fuser -k 8501/tcp

restart: stop start
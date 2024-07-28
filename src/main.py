from service import Service
import uvicorn

if __name__ == "__main__":
    service: Service = Service()
    uvicorn.run(service.app, host="0.0.0.0", port=8084)

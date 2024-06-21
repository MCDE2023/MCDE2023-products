import os
import uvicorn

if __name__ == '__main__':
    port: int = int(os.environ.get('PORT', 8080))
    uvicorn.run('app.main:app', host='127.0.0.1', port=port, reload=True)
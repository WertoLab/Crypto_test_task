# Service for getting transactions of ETH

## Instruction
### Clone repository
```bash
git clone https://github.com/WertoLab/Crypto_test_task.git
```

### Enter to directory
```bash
cd Crypto_test_task
```



### Create docker image
```bash
docker build . -t transactions_app:latest 
```

### Run
```
docker run -d -p 8000:8000 -t transactions_app:latest 
```

```bash
Check swagger by http://127.0.0.1:8000/docs 
```

### Request example
```json
{
  "datetime": "Tue, 23 Apr 2024 23:20:45",
  "integer": 2,
  "entities_limit": 3,
  "offset": 2
}
```
import boto3

def create_sqs_queue(queue_name='MinhaFilaSQS'):
    """Cria uma fila SQS e retorna a URL da fila."""
    sqs_client = boto3.client('sqs')

    try:
        response = sqs_client.create_queue(QueueName=queue_name)
        queue_url = response['QueueUrl']
        print(f"Fila SQS '{queue_name}' criada com sucesso: {queue_url}")
        return queue_url
    except Exception as e:
        print(f"Erro ao criar fila SQS: {e}")

# Exemplo de uso
# create_sqs_queue('MinhaFilaSQS')

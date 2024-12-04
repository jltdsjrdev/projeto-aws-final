import boto3

def create_sns_topic(topic_name='MeuTopicoSNS', region='us-east-1'):
    """
    Cria um tópico SNS e retorna o ARN do tópico.
    
    Args:
        topic_name (str): Nome do tópico SNS a ser criado.
        region (str): Região onde o tópico será criado. Padrão: 'us-east-1'.
    
    Returns:
        str: ARN do tópico SNS criado.
    """
    sns_client = boto3.client('sns', region_name=region)

    try:
        response = sns_client.create_topic(Name=topic_name)
        topic_arn = response['TopicArn']
        print(f"Tópico SNS '{topic_name}' criado com sucesso.")
        print(f"ARN do Tópico: {topic_arn}")
        return topic_arn
    except Exception as e:
        print(f"Erro ao criar tópico SNS: {e}")
        return None

# Exemplo de uso
if __name__ == "__main__":
    topic_arn = create_sns_topic('MeuTopicoSNS')
    if topic_arn:
        print(f"Tópico criado com ARN: {topic_arn}")
    else:
        print("Falha ao criar o tópico SNS.")

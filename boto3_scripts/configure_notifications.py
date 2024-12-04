import boto3

def configure_bucket_notifications(bucket_name, topic_arn):
    """Configura notificações para um bucket S3 para um tópico SNS."""
    s3_client = boto3.client('s3')

    notification_configuration = {
        'TopicConfigurations': [
            {
                'TopicArn': topic_arn,
                'Events': ['s3:ObjectCreated:*']
            }
        ]
    }

    try:
        s3_client.put_bucket_notification_configuration(
            Bucket=bucket_name,
            NotificationConfiguration=notification_configuration
        )
        print(f"Notificações configuradas no bucket '{bucket_name}' com sucesso.")
    except Exception as e:
        print(f"Erro ao configurar notificações no bucket: {e}")

# Exemplo de uso
# configure_bucket_notifications('meu-bucket', 'arn:aws:sns:us-east-1:123456789012:MeuTopicoSNS')

# Configuração do security group para acesso SSH e API
resource "aws_security_group" "sec_demoday_api" {
  name        = "sec-demoday-api"
  description = "Allow incoming SSH, HTTP, and HTTPS connections."

  # Inbound - SSH
  ingress {
    description = "SSH to EC2"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # Inbound - API
  ingress {
    description = "API to EC2"
    from_port   = 8000
    to_port     = 8000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # Outbound - Permitir todas as conexões
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "sec-demoday-api"
  }
}

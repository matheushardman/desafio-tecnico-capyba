resource "aws_instance" "api_demoday" {
  ami                    = "ami-0a0e5d9c7acc336f1"
  instance_type          = "t2.micro"
  key_name               = aws_key_pair.user_ec2_key.key_name
  vpc_security_group_ids = [aws_security_group.sec_demoday_api.id]  
  user_data              = file("script.sh")

  tags = {
    Name = "api-demoday"
  }
}
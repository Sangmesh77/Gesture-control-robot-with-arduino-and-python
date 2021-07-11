void setup() 
{
  pinMode(7,OUTPUT);
  //digitalWrite(7,LOW);  
  
  pinMode(3,OUTPUT);
  //digitalWrite(3,LOW);  
  
  pinMode(5,OUTPUT);
  //digitalWrite(5,LOW);  
  Serial.begin(9600);
}

void loop() 
{
  if(Serial.available() > 0)
 {
    
   // Serial.read();
   //Serial.setTimeout(1000);
      if(Serial.read()=='f') 
    {
     
      digitalWrite(7,HIGH);
      digitalWrite(1,LOW);
      digitalWrite(3,LOW);
      delay(200);
      digitalWrite(7,LOW);
      
    }
    
     if(Serial.read()=='h')
      {
      digitalWrite(3,HIGH);
      digitalWrite(1,LOW);
      digitalWrite(7,LOW);
      delay(50);
       digitalWrite(3,LOW);
      }
    if(Serial.read()=='p')
      {
      digitalWrite(5,HIGH);
      digitalWrite(1,LOW);
      digitalWrite(3,LOW);
      delay(100);
      digitalWrite(5,LOW);
      }
    else
    {
      digitalWrite(5,LOW);
      digitalWrite(1,LOW);
      digitalWrite(3,LOW);
      delay(150);
      
      }  
   }
 

    else
    {
      digitalWrite(7,LOW);
      digitalWrite(3,LOW); 
      digitalWrite(5,LOW);
  
    }    
    
    }
    


    //delay(10000);
    

/* 
 _______________________________________________________________________
|  Componente        | Pinos ESP32 DEVKITV1           | Alimentação    |
| ------------------ | ------------------------------ |----------------|
| Display            | D18 (SCK), D23 (SDA),          |                |
|      ST7735(SPI)   |   D5 (CS), D2 (A0), D4 (RST).  | 3 volts        |
|                    |                                |                |
| Encoder rotativo   | D34 (CLK), D35 (DT), D32 (SW). | 3 volts        |
|                    |                                |                |
| Servo motores      | D25 (sinal)                    | 5 volts        |
|                    |                                |                |
| Telêmetro a laser  | 22 (SCL), D23 (SDA)            | 3 volts        |
|                    |                                |                |
| RGB led            | D12 (R), D13 (G),D14 (B).      |   X            |
|                    |                                |                |
| Leitura bateria    | PWM D33                        |   X            |
|____________________|________________________________|________________|

Em uso: 2, 4, 5, 12, 13, 14, 18, 23, 25, 32, 33, 34, 35.
Sobra: 15, 16, 17, 19, 21, 22, 26, 27, VN, VP, EN, TX0, RX0.

Telêmetro a laser - Lerá o nível da ração
Leitura da bateria - necessária pois o sistema não vai ser ligado diretamente na tomada
RGB led - informar necessidades do sistema rapidamente
Display - funcionará como o console
Encoder - input e navegação dentro do sistema
Servos - mover o dispenser de comida

*/
//-----------------------------------------------------------------Wifi
#include <WiFi.h> //CONEXÃO WIFI
#include <WiFiUdp.h> //COMUNICAÇÃO VIA NTP
#include <NTPClient.h> //LADO CLIENTE - RECEBER
const char* ssid = "Comedouro Inteligente";
const char* senha = "@NatsuAgnes2025";

//----------------------------------------------------------------------------Display SPI
// 0 <= X <= 239              0 <= Y <= 319
// rgb: uint16_t cor = tft.color565(0, 0, 0);   // vermelho
#include <Adafruit_GFX.h>
#include <Adafruit_ST7735.h>
#define Dis_CS D5
#define Dis_A0 D2
#define Dis_RST D4

Adafruit_ST7735 Display = Adafruit_ST7735(Dis_CS, Dis_A0, Dis_RST);

//---------------------------------------------------------Encoder
#include "AiEsp32RotaryEncoder.h"
#define En_DT_b D35 // pino dados do encoder
#define En_SW_btn D32 //pino botão do encoder
#define En_CLK_a D34 //pino clock do encoder
#define En_pss 4 //passos do encoder

AiEsp32RotaryEncoder Encoder = AiEsp32RotaryEncoder(En_CLK_a, En_DT_b, En_SW_btn, -1, En_pss);

void IRAM_ATTR readEncoderISR(){ Encoder.readEncoder_ISR(); } //pesquisar para que serve esse trecho
//-------------------Sensor laser
#include <Adafruit_VL53L0X.h>
//-------------------Servos
#define Servos D25
//-------------------Pilha A
#define Baterias D33
//-------------------Led RGB
#define LedR D12
#define LedG D13
#define LedB D14
//-------------------RTC interno
#include <time.h>
#include <ArduinoJson.h>



void setup() {
    //------------------------------Begin e init
    Serial.begin(9600);
    Encoder.begin();
    WiFi.begin(ssid, senha)
    timeClient.begin()
    tft.initR(INITR_BLACKTAB)
    
    //------------------------------Configurações
    Encoder.setup(readEncoderISR);
    Encoder.setBoundaries(0, 9, true); //minimo, maximo e se terá loop
    Encoder.setAcceleration(250);
    //pinMode(Servos, OUTPUT);
    //------------------------------Chamadas Iniciais
    delay(5000); //espera 5 segundos

}
void loop(){
  if (WiFi.status() == WL_CONNECTED) {
    timeClient.update();
    Serial.println(timeClient.getFormattedTime());
  }
  else{
    int hora = configurar_horario();
    int minuto = configurar_horario();
    Serial.print(hora);
    Serial.print(":");
    Serial.println(minuto);
  }
  /*
   hora = funcao de acompanhar o rtc pela placa
   if (hora == 11 || hora == 16 || hora == 20){
      alimentar();
      break;
   delay(5000);
   }
*/}

int configurar_horario(){
    int A = -1;
    int B = -1;
    while (B < 0){
      if (A < 0 && B == -1){
        if (Encoder.isEncoderButtonClicked()){
          A = (A + 1) + (Encoder.readEncoder() * 10);
          Serial.print("A = ");
          Serial.println(A);
          delay(4000);
        }
      }
      if (B < 0 && A >= 0){
        if (Encoder.isEncoderButtonClicked()){
          B = (B + 1) + Encoder.readEncoder();
          Serial.print("B = ");
          Serial.println(B);
          delay(4000);
        }
      }
      if (B >= 0){
        break;
      }
      Serial.print("Usar: ");
      Serial.println(Encoder.readEncoder());
      yield();
    }//fim while  
    Serial.print("Fim da Configuração");
    return A+B;
}
void alimentar(){
  servo.digitalWrite
}
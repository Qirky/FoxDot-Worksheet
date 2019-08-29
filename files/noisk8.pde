import oscP5.*;

OscP5 oscP5;

boolean bass_flag = false;
boolean dirt_flag = false;
boolean blip_flag = false;
boolean space_flag =false;
boolean bell_flag =false;



void setup() {
size(800, 800);
background(155);

oscP5 = new OscP5(this,12345);

}

void draw() {

if(bass_flag){
fill( random(204, 1), 29, 20 , 211);
triangle (random(0, 800), random(0, 800),200, 300, 59, 55);
}


if(dirt_flag){

fill (random( 20,102), 29, 20 , 211);
triangle(random(0,800), random(800,0), 200, 300, 59, 55);
}


if(blip_flag){ 

fill (random( 20,202), 240,102, 200);
triangle(random(0,800), random(0,800), 55, 55, 20 ,80);
}



if (space_flag){

fill (random(250,40), 10,102, 50);
triangle(random(0,2000), random(700,3000), 55, 55, 300, 400);
}

if (bell_flag){

fill (random(250,50), 0,102, 25);
quad(random(0,8000), 300, 400, 0, 440, 660, 0, 9000);
}



bass_flag = false;
space_flag=false;
dirt_flag = false; 
blip_flag=false;
bell_flag=false;
}
void oscEvent(OscMessage msg) {

if(msg.checkAddrPattern("/s_new")==true) {
if(msg.get(0).stringValue().equals("bass")){
println("bass");
bass_flag = true;
}
if(msg.get(0).stringValue().equals("play1") || msg.get(0).stringValue().equals("play2")){
if(msg.get(67).floatValue()==1.0){
//bd
println("bd");
}else{
//perc
println("perc");

}
}
}

if(msg.checkAddrPattern("/s_new")==true) {
if(msg.get(0).stringValue().equals("dirt")){
println("dirt");
dirt_flag = true;
}
if(msg.get(0).stringValue().equals("play3") || msg.get(0).stringValue().equals("play2")){
if(msg.get(67).floatValue()==1.0){
//bd
println("gf");
}else{
//perc
println("sic");

}
}
}


if(msg.checkAddrPattern("/s_new")==true) {
if(msg.get(0).stringValue().equals("blip")){
println("blip");
blip_flag = true;
}
if(msg.get(0).stringValue().equals("play3") || msg.get(0).stringValue().equals("play2")){
if(msg.get(67).floatValue()==1.0){
//bd
println("yyf");
}else{
//perc
println("snn");

}
}
}

if(msg.checkAddrPattern("/s_new")==true) {
if(msg.get(0).stringValue().equals("space")){
println("V");
space_flag = true;
}
if(msg.get(0).stringValue().equals("play5") || msg.get(0).stringValue().equals("play6")){
if(msg.get(67).floatValue()==1.0){
//bd
println("yyf");
}else{
//perc
println("snn");

}
}
}
if(msg.checkAddrPattern("/s_new")==true) {
if(msg.get(0).stringValue().equals("bell")){
println("bell");
bell_flag = true;
}
if(msg.get(0).stringValue().equals("play5") || msg.get(0).stringValue().equals("play6")){
if(msg.get(67).floatValue()==1.0){
//bd
println("bell");
}else{
//perc
println("bell");

}
}
}

}

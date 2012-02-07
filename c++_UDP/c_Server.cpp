/*
* Author: Theo
* Date: 10/01/2012
 */

#include "PracticalSocket.h" // For UDPSocket and SocketException
#include <iostream>          // For cout and cerr
#include <cstdlib>           // For atoi()
#include "RacerData.h"
#include <sstream>

const int ECHOMAX = 4096;     // Longest string to echo

string convert(float speed, float brake, float gas, float clutch, int gear, int distance, int time, float x, float y, float z, float ax, float ay, float az, float steering){
	stringstream ss (stringstream::in | stringstream::out);
	ss<<speed<<";"<<brake<<";"<<gas<<";"<<clutch<<";"<<gear<<";"<<distance<<";"<<time<<";"<<x<<";"<<y<<";"<<z<<";"<<ax<<";"<<ay<<";"<<az<<";"<<steering;
	return ss.str();
}

int main(int argc, char *argv[]) {

  if (argc != 3) {                  // Test for correct number of parameters
    cerr << "Usage: " << argv[0] << " <<Game Port> " << " <Destination Port> " <<  endl;
    exit(1);
  }
  int no = 0;
  unsigned short echoServPort = atoi(argv[2]);     // First arg:  local port
  unsigned short destPort = 7011;//atoi(argv[2]); 	

  try {
    UDPSocket sock(echoServPort);                	
    //int echoBuffer[ECHOMAX];         // Buffer for echo string
    RDashData echoBuffer[ECHOMAX];
    int recvMsgSize;                  // Size of received message
    string sourceAddress;             // Address of datagram source
    unsigned short sourcePort;        // Port of datagram source
    for (;;) {  // Run forever
      // Block until receive message from a client
      recvMsgSize = sock.recvFrom(echoBuffer, ECHOMAX, sourceAddress, 
                                      sourcePort);
  
    cout << "Received packet from " << sourceAddress << ":" 
           << sourcePort << endl;

if ((echoBuffer[0].rpm != 0) && (echoBuffer[0].engineState != 0))
{  
    cout << "Time " << echoBuffer[0].time <<endl;
    cout << "Speed " << echoBuffer[0].vehSpeed * 3.63 <<endl;
    cout << "Gear " << echoBuffer[0].gearEngaged <<endl;
    cout << "rpm " << echoBuffer[0].rpm << "  state "<<echoBuffer[0].engineState<<endl;
    cout << "distance " << echoBuffer[0].lapDistance <<endl;
    cout << "car " << echoBuffer[0].carName <<endl;
    cout << "GFORCE lat"<<echoBuffer[0].gforceLat<< "long"<<echoBuffer[0].gforceLon<<endl;
    cout << "Pos x "<<echoBuffer[0].pos.x<< "y "<<echoBuffer[0].pos.y<< " z "<< echoBuffer[0].pos.z<<endl;
    cout<<"Test"<<endl;
    cout <<echoBuffer[0].steering<< "  "<<echoBuffer[0].throttle<<"  "<<echoBuffer[0].brakes<<"  "<<echoBuffer[0].clutch<<endl;
    cout << "Acc x "<<echoBuffer[0].acc.x<< "y "<<echoBuffer[0].acc.y<< " z "<< echoBuffer[0].acc.z<<endl;
    cout<<"steeritng "<<echoBuffer[0].steering<<endl;
    cout<<endl;

string message = convert(echoBuffer[0].vehSpeed * 3.63, 
			echoBuffer[0].brakes, 
			echoBuffer[0].throttle,
			echoBuffer[0].clutch, 
			echoBuffer[0].gearEngaged,
			echoBuffer[0].lapDistance,
			echoBuffer[0].time,
			echoBuffer[0].pos.x,
			echoBuffer[0].pos.y,
			echoBuffer[0].pos.z,
			echoBuffer[0].acc.x,
			echoBuffer[0].acc.y,
			echoBuffer[0].acc.z,	
			echoBuffer[0].steering);

cout<<message<<endl;;
char* s = new char[message.size()];
 
for (int i=0; i<message.size(); i++){
	s[i] = message[i];
}


 	string destAddr= "192.168.1.98";	
        sock.sendTo(s, message.size(), destAddr, destPort);	
	cout<<"SEND TO: " << destAddr<<":"<<destPort<<endl;
	cout<<++no<<endl;	
    }
}
  } catch (SocketException &e) {
    cerr << e.what() << endl;
    exit(1);
  }
  return 0;
}



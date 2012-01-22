/*
 *   C++ sockets on Unix and Windows
 *   Copyright (C) 2002
 *
 *   This program is free software; you can redistribute it and/or modify
 *   it under the terms of the GNU General Public License as published by
 *   the Free Software Foundation; either version 2 of the License, or
 *   (at your option) any later version.
 *
 *   This program is distributed in the hope that it will be useful,
 *   but WITHOUT ANY WARRANTY; without even the implied warranty of
 *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *   GNU General Public License for more details.
 *
 *   You should have received a copy of the GNU General Public License
 *   along with this program; if not, write to the Free Software
 *   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
 */

#include "PracticalSocket.h" // For UDPSocket and SocketException
#include <iostream>          // For cout and cerr
#include <cstdlib>           // For atoi()
#include "RacerData.h"
#include <sstream>

const int ECHOMAX = 4096;     // Longest string to echo

string convert(float speed, float brake, float gas, float clutch, int gear, int distance, int time){
	stringstream ss (stringstream::in | stringstream::out);
	ss<<speed<<";"<<brake<<";"<<gas<<";"<<clutch<<";"<<gear<<";"<<distance<<";"<<time;
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
    cout <<echoBuffer[0].steering<< "  "<<echoBuffer[0].throttle<<"  "<<echoBuffer[0].brakes<<"  "<<echoBuffer[0].clutch<<endl;
    cout<<endl;

string message = convert(echoBuffer[0].vehSpeed * 3.63, 
			echoBuffer[0].brakes, 
			echoBuffer[0].throttle,
			echoBuffer[0].clutch, 
			echoBuffer[0].gearEngaged,
			echoBuffer[0].lapDistance,
			echoBuffer[0].time);

cout<<message<<endl;;
char* s = new char[message.size()];
 
for (int i=0; i<message.size(); i++){
	s[i] = message[i];
}


 	string destAddr= "192.168.1.98";
	string msg[1];
	msg[0] = "hello world";			
      sock.sendTo(s, message.size(), destAddr, destPort);	
	cout<<"SEND TO: " << destAddr<<":"<<destPort<<endl;
	cout<<++no<<endl;	
    }
}
  } catch (SocketException &e) {
    cerr << e.what() << endl;
    exit(1);
  }
  // NOT REACHED
  return 0;
}



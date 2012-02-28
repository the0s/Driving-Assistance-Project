%Convert Racer text to variable arrays
%Author: Theos
%22/02/2012
%Text file data:Speed,brakes,gas,clutch,gear,distance,time, x, y ,z, x-acc, y-acc,z-acc,steering

function [A,check, speed, brakes,gas,clutch,gear,distance,time, position3d, acceleration3d,steering] = RacerToMatlab(filename)
    fid = fopen(filename);
    A = fscanf(fid,'%g %g %g %g %g %g %g %g %g %g %g %g %g %g %g',[15 inf] );
    fclose(fid);
    check= A(1,:);
    speed = A(2,:);
    brakes = A(3,:);
    gas = A(4,:);
    clutch = A(5,:);
    gear = A(6,:);
    distance = A(7,:);
    time = A(8,:);
    position3d = A(9:11,:);
    acceleration3d = A(12:14,:);
    steering = A(15,:);
    %PLOTTING
    figure
    subplot(3,3,1);
    plot(speed);
    title('Speed');
    
    subplot(3,3,2);
    plot(brakes);
    title('Brake');
    
    subplot(3,3,3);
    plot(gas);
    title('Gas')
    
    subplot(3,3,4);   
    plot(clutch);
    title('Clutch')
    
    subplot(3,3,5);
    plot(gear);
    title('Gear')
    
    subplot(3,3,6);    
    plot(distance);
    title('Distance')
   
    subplot(3,3,7);    
    plot(check);
    title('In-Route')
    
    subplot(3,3,8);
    plot3(position3d(1,:),position3d(2,:),position3d(3,:))
    title('Position3d')
    
    subplot(3,3,9);    
    plot3(acceleration3d(1,:),acceleration3d(2,:),acceleration3d(3,:))
    title('Acceleration3d')
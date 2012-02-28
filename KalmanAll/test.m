% Make a point move in the 2D plane
% State = (x y xdot ydot). We only observe (x y).

% This code was used to generate Figure 17.9 of "Artificial Intelligence: a Modern Approach",
% Russell and Norvig, 2nd edition, Prentice Hall, in preparation.

% X(t+1) = F X(t) + noise(Q)
% Y(t) = H X(t) + noise(R)

ss = 15; % state size
os = 15; % observation size
F = eye(ss);
H = eye(ss);
Q = 0.1*eye(ss);
R = 1*eye(os);
initx = A(:,1);
initV = 10*eye(ss);

x = A(9:10,:);
%seed = 9;
%rand('state', seed);
%randn('state', seed);
%T = 10;
%[x,y] = sample_lds(F, H, Q, R, initx, T);

[xfilt, Vfilt, VVfilt, loglik] = kalman_filter(A, F, H, Q, R, initx, initV);
[xsmooth, Vsmooth] = kalman_smoother(A, F, H, Q, R, initx, initV);

dfilt = A([9 10],:) - xfilt([9 10],:);
mse_filt = sqrt(sum(sum(dfilt.^2)))

dsmooth = A([9 10],:) - xsmooth([9 10],:);
mse_smooth = sqrt(sum(sum(dsmooth.^2)))



subplot(2,1,1)
hold on
plot(x(1,:), x(2,:), 'ks-');
plot(A(9,:), A(10,:), 'g*');
plot(xfilt(9,:), xfilt(10,:), 'rx:');
%for t=1:T, plotgauss2d(xfilt(9:10,t), Vfilt(9:10, 9:10, t)); end
hold off
legend('true', 'observed', 'filtered', 0)
xlabel('X1')
ylabel('X2')

subplot(2,1,2)
hold on
plot(x(1,:), x(2,:), 'ks-');
plot(A(9,:), A(10,:), 'g*');
plot(xsmooth(9,:), xsmooth(10,:), 'rx:');
%for t=1:T, plotgauss2d(xsmooth(9:10,t), Vsmooth(9:10, 9:10, t)); end
hold off
legend('true', 'observed', 'smoothed', 0)
xlabel('X1')
ylabel('X2')




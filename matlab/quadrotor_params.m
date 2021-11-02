%% Quadrotor Parameters

m = 1; % mass of quadrotor [kg]
g = 9.80665; % gravitational acceleration [kg/s^2]
d_x = 0.1; % x-component of the induced drag coefficient 
d_y = 0.1; % y-component of the induced drag coefficient 
A_1c = 0.2; % 1st harmonic, cosine coefficient for the blade flapping motion 
            % steady-state solution
A_1s = 0.3; % 1st harmonic, sine coefficient for the blade flapping motion 
            % steady-state solution
r = 0.1; % radius of rotor blade [m]
A = pi * r^2; % rotor disc area [m^2]
d = 0.5; % drone arm length [m]
I = [[1, 0, 0], [0, 1, 0], [0, 0, 3]]; % constant inertia matrix [kg/m^2]
rho = 1.225; % air density at corresponding altitude [kg/m^3]
C_T = 0.1115; % thrust coefficient for rotor
C_Q = 0.0223; % reaction torque coefficient for rotor


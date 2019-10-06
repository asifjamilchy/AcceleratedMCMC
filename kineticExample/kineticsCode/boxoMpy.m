function ymod=boxoMpy(data,theta)
% model function for the boxo example
%disp('inside boxoM');
%disp(data);
%disp(theta);
% starting concentrations are at the end of the parameter vector
y0 = theta(end-1:end);
% time is the first column of data.ydata
t  = data(:,1);

% if using lsode mex, save parameter vector in global variable
global lsode_data
lsode_data = theta;

if exist('lsode_mex') == 3
  %disp('lsode exists');
  % use much faster mex code for ode
  [tout,y] = lsode22('internal',t,y0);
else
  %disp('calling boxoODE...');
  [tout,y] = ode45(@boxoODE,t,y0,theta);
  %disp('boxoODE done.');
end
%disp(tout);
%disp(y);
ymod = y;

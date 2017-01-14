st=0;
en=3;
x=st:0.1:en;

y = zeros(1,length(x));
y(1) = 1;
for i=1:(length(x)-1)
    y(i+1) = runge(x(i), y(i), 0.1, 0.05, 1e-5);
end

[t,z] = ode45(@f, [st,en], 1);
plot(x,y,t,z);
plottools;
grid on;
xlabel(t);
ylabel(y);
title('y" = -yt');
legend('calc', 'ode');
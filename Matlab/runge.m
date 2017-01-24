function y = runge(t0, y0, dt, h, tol)

flag = 1;
t = t0;
y = y0;
while (t < t0 + dt)
    k1 = h * f(t, y);
    k2 = h * f(t + 1/4*h,   y + 1/4*k1);
    k3 = h * f(t + 3/8*h,   y + 3/32*k1 +       9/32*k2);
    k4 = h * f(t + 12/13*h, y + 1932/2197*k1 -  7200/2197*k2 +  7296/2197*k3);
    %k5 = h * f(t + h,       y + 439/216*k1 -    8*k2 +          3680/513*k3 - 845/4104*k4);
    %k6 = h * f(t + h/2,     y - 8/27*k1 +   2*k2 - 3544/2565*k3 + 1859/4104*k4 - 11/40*k5);
        
    y = y + 25/216*k1 + 1408/2565*k3 + 2197/4104*k4;
    if (flag)
        z = y + 16/135*k1 + 6656/12825*k3 + 28561/56430*k4;
    end
    if (flag && abs(y - z) > tol)
        t = t0;
        y = y0;
        h = h * (tol * h/2/abs(z-y))^0.25;
    else
        t = t + h;
        flag = 0;
    end
end

x = load('ex2x.dat');
x = [ones(length(x), 1), x];
y = load('ex2y.dat');

theta = ones(2, 1);

[theta, J_hist] = gradientd(x, y, theta, 0.01, 1000)

w = computeCost(x, y, theta)

plot(x(:, 2), y, 'ro')
hold on;
plot([2,8],[theta(1)+theta(2)*2, theta(1)+theta(2)*8]);

pause;


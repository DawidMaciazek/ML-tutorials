function [theta, J_hist] = gradientd(x, y, theta, alpha, iters)

data_size = length(y);
features_size = length(theta);
J_hist = zeros(iters, 1);


for iter = 1:iters
	theta_grad_sum = zeros(features_size, 1);

	for i = 1:data_size
		theta_grad_sum = theta_grad_sum + (x(i, :)*theta -y(i))*(x(i, :).');
	end

	theta = theta - (alpha/data_size) * theta_grad_sum;
	cr_cost = computeCost(x, y, theta)
	J_hist(iter) = cr_cost;

end
end

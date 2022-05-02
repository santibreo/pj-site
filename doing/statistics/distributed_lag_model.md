## Distributed Lag Model (DL)

$$
y_{t} = f(x_{t}, x_{t-1}, x_{t-2}, \ldots)  \rightarrow y_{t}=\alpha + \sum_{i=0}^q \beta_i \cdot x_{t-i} + \varepsilon_{t}
$$

### Assumptions

1. $y_t$ and $x_t$ are stationary random variables and $\varepsilon_t$ is independent of $x_t$

2.  $\overline{\varepsilon_t} = 0$ and $\text{var}(\varepsilon_t) = \sigma^2$

3. $\text{cov}(\varepsilon_t, \varepsilon_s) = 0$ if $t \neq s$

4. $\varepsilon_t \sim N(0, \sigma^2)$

### R Example

$$
 \begin{aligned} \rho_{t} = \frac{\text{cov}(x_{t}, x_{t-1})}{\sqrt{\text{var}(x_{t})\text{var}(x_{t-1})}} = \frac{\text{cov}(x_{t}, x_{t-1})}{\text{var}(x_{t})} \end{aligned}
$$

$$
\begin{aligned}
\widehat{\text{cov}}(x_{t}, x_{t-1}) &= \frac{1}{T-1}\sum_{t=2}^{T}{(x_{t}-\bar{x})(x_{t-1}-\bar{x})}\\
\widehat{\text{var}}(x_{t}) &= \frac{1}{T-1}\sum_{t=1}^{T}{(x_{t}-\bar{x})^{2}} \end{aligned}
$$

$$
\begin{aligned}
Z = \frac{r_{k}-0}{\sqrt{1/T}} = \sqrt{T} \cdot r_{k} \sim N(0,1)
\end{aligned}
$$

$$
\begin{aligned} \text{var}(b_{2}) & = \sum_{t}{w_{t}^{2}\text{var}(e_{t})} + \sum_{t \neq s}{\sum{w_{t}w_{s}\text{cov}(e_{t}, e_{s})}} \\ & = \sum_{t}{w_{t}^{2}\text{var}(e_{t})} \Bigg[1+\frac{\sum_{t \neq s}{\sum{w_{t}w_{s}\text{cov}(e_{t}, e_{s})}}}{\sum_{t}{w_{t}^{2}\text{var}(e_{t})}}\Bigg] \end{aligned}
$$

$$
\begin{aligned}
\rho_{k} & =\text{corr}(e_{t}, e_{t-k})=\frac{\text{cov}(e_{t}, e_{t-k})}{\sqrt{\text{var}(e_{t})\text{var}(e_{t-k})}} = \frac{\text{cov}(e_{t}, e_{t-l})}{\text{var}(e_{t})} \\
& = \frac{\rho^{k}\sigma_{v}^{2}/(1-\rho^{2})}{\sigma_{v}^{2}/(1-\rho^{2})} \\
& = \rho^{k} 
\end{aligned}
$$

## Autoregresive Distributed Lagged Models (ARDL)

$$
 \begin{aligned}
 y_{t} = f(y_{t-1}, y_{t-2}, \ldots, x_{t}, x_{t-1}, x_{t-2}, \ldots)
 \end{aligned}
$$

$$
\begin{aligned}
 y_{t} = \alpha + \sum_{i=0}^{p} \theta_i y_{t-i} + \sum_{j=0}^{q}{\beta_{j}x_{t-j}+e_{t}} \end{aligned}
$$



Error term dependent on itself in previous periods $\rightarrow$ **serially correlated or autocorrelated**.

$$
 \begin{aligned}
 y_{t} = f(x_{t}) + \varepsilon_{t} && \varepsilon_{t}=g(\varepsilon_{t-1}) 
 \end{aligned}
$$

### Possible criteria

* If serial correlation in errors has not been removed, LSE is biased in small and large samples. Check it with correlogram or Lagrange multiplier tests

* What values of $p$ and $q$ minimize information criteria such as AIC, SC or BIC
  
  $$
  \begin{aligned}
\text{AIC}=\ln{\bigg(\frac{SSE}{T}\bigg)} + \frac{2K}{T}
\end{aligned}
  $$

## Least Squares Assumptions

$$
\begin{aligned}
\text{cov}(y_{t}, y_{s}) = \text{cov}(e_{t}, e_{s}) = 0 && \text{for} &&  t \neq s
\end{aligned} 
$$

**Stationarity**: Variables are stationary, which means that a variable is not explosive, nor trending and not wandering aimlessly without returning to its mean.







































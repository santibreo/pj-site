:draft: false
:date: 23-11-2020


=================================
Rent or buy, that is the question
=================================

I have just make some algebra to understand how the amortization works and
which is the best way to pay a Loan. A few definitions are necessary to
understand the following calculus.

* :math:`N` = Notional: **Initial** amount borrowed by the lender.
* :math:`O_k` = Outstanding: Remaining or unpaid loan amount.
* :math:`A_k` = Amortization: Portion of the nominal amount that is paid in each
  payment.
* :math:`r_k` = Interest Rate: Annualized interest rate applied to the Loan. It
  could be fixed or variable.
* :math:`\Delta t_k` = Year fraction: Fraction of the year since last payment.
* :math:`n` = Total number of payments: The number of payments in which the loan is
  expected to be settled.
* :math:`I_k` = Interest Payment. Interest to be paid on each payment.

  .. math::

      I_k = O_{k-1} \cdot r_k \cdot \Delta t_k


3 are the most common ways to amortise a loan:

1. Bullet: During the life of the loan only interest is paid and at the end the
   nominal is settled.
2. Constant: The same nominal amount is amortised in each payment.
3. French: A minimally sophisticated formula is applied in which several of the
   defined variables intervene to calculate the fee to be paid, which includes
   interest:

   .. math::

      P_k = A_k + I_k = O_{k-1} \cdot \frac{r_k \cdot \Delta t_k}{1-(1 + r_k \cdot \Delta t_k)^{n-k+1}}


In this post I have focus on the methods that have payments during the
loan's life. So I won't concern about bullet method, which amortization is
pretty straightforward.

Due to the amortizations selected, each amortization depends on the remaining
amount after each payment, which we can write as:

.. math::

   A_k = \alpha_k \cdot O_{k-1}\\
   with\ O_0 = N

For the successive payments:

.. math::

   \begin{aligned}
   A_1 &= N \cdot \alpha_1\\
   A_2 &= O_1 \cdot \alpha_2 = N(1 - \alpha_1) \cdot \alpha_2 \\
   A_3 &= O_2 \cdot \alpha_3 = N(1 - \alpha_1)(1 - \alpha_2) \cdot \alpha_3 \\
   \ldots
   \end{aligned}


Which reveals a clear pattern, the Outstanding can be written as:

.. math::

   O_k = N \cdot \prod_{i=1}^{k}(1 - \alpha_i)

So now we can just focus on :math:`\alpha`, that depends on the amortization
type.

Constant (warmup)
-----------------

The constant amortization is not a big deal, so here I am showing how to work
with it as a way to get used to the method, but the **french** amortization
is the one that motivate this post. First of all the :math:`\alpha`, which comes
from the amortization definition:

.. math::

   A_k = O_{k-1} \cdot \frac{1}{n-k+1} \rightarrow \alpha_k = \frac{1}{k-n-1}

So, as it has been shown:

.. math::

   \begin{aligned}
   O_k &= N \cdot \prod_{i=1}^{k} \left(1 - \frac{1}{n-i+1}\right)\\
   O_k &= N \cdot \prod_{i=1}^k \frac{n-i}{n-i+1}\\
   \end{aligned}


Here the telescopic property for the product: :math:`\prod_{i=1}^{k} \frac{a_i}{a_{i-1}} = \frac{a_k}{a_0}`
is used to simplify the expression with :math:`a_i = n - i`:

.. math::

   O_k = N \cdot \left(1 - \frac{k}{n}\right)

Now it becomes obvious that at :math:`k=n` the Outstanding is 0, as it should. We can
evaluate the amortization making finite differences:

.. math::

   A_k = \frac{N}{n}

So the Amortization does not depend on :math:`k` (that's probably why it is called
constant), if there are not prepayments, the amortised amount is always the
same. Finally we should evaluate how this combines with the interest payment and
the total payment. For simplicity I am going to use
:math:`\beta_k = r_k \cdot \Delta t_k`.

.. math::

   \begin{aligned}
   I_k = O_{k-1} \cdot \beta_k = N \cdot \beta_k \cdot \frac{n-k+1}{n}\\
   P_k = \frac{N}{n} \cdot \left(1 + \beta_k \cdot (n-k+1) \right)
   \end{aligned}

In view of the formula it is clear that the instalment to be paid declines
linearly with the number of payments due only to the payment of interest.
If we suppose a fixed annual Interest Rate (:math:`r`) of 3%, a monthly payment
frequency (it is :math:`\beta = 0.0025`) and 20 years as time to maturity of the
loan (:math:`n=240`); we can evaluate what percentage of each installment will
represent the interest:

.. math::

   IR_k = \frac{I_k}{P_k} = \frac{\beta \cdot (n-k+1)}{1 + \beta \cdot (n-k+1)}

But to make the reasoning cleaner, we will calculate the percentage of the
amount amortised, in this way the sum of these percentages will give the
percentage of interest paid on the nominal, since the sum of the amounts
amortised is the nominal:

.. math::

   TIR = \sum_{i=1}^n\frac{I_i}{N} = \frac{1}{n}\sum_{i=1}^n \beta_i \cdot (n-i+1)

Assuming that :math:`\beta` is constant (as in our example):

.. math::

   TIR = \frac{\beta \cdot (n+1)}{2}

Which, with the figures given above, totals **30.125%**. So you maybe want to
think twice before taking a loan with this amortization type.


French
------

This is the amortization type I get most insterested in, because it is the most
common in mortgage loans accessed by individuals. As far as I know this method
was developed to keep the payment constant (almost), which is what people is
looking for when they are asking for money.

To follow the previous path first we have to remove the interests from the
payment formula, using the previously given :math:`\beta_k` definition:

.. math::

   \begin{aligned}
   A_k &= O_{k-1} \cdot \left(\frac{\beta_k \cdot (1 + \beta_k)^{n-k+1}}{(1 + \beta_k)^{n-k+1} - 1} - \beta_k\right) = O_{k-1} \cdot \left(\frac{\beta_k}{(1 + \beta_k)^{n-k+1} - 1}\right) \\
   \alpha_k &= \frac{\beta_k}{(1 + \beta_k)^{n-k+1} - 1}
   \end{aligned}

Now I can apply the cumulative product formula that has been developed previously:

.. math::

   \begin{aligned}
   O_k &= N \cdot \prod_{i=1}^k \left(1 - \frac{\beta_i}{(1 + \beta_i)^{n-i+1} - 1}\right) \\
   &= N \cdot \prod_{i=1}^k \left(\frac{(1 + \beta_i)\left((1 + \beta_i)^{n-i} - 1\right)}{(1 + \beta_i)^{n-i+1} - 1}\right) \\
   &= N \cdot \left[ \prod_{i=1}^k (1+\beta_i) \cdot \frac{(1 + \beta_i)^{n-i} - 1}{(1 + \beta_i)^{n-i+1} - 1} \right]
   \end{aligned}

This expression doesn't allow further simplification because :math:`\beta_k` is
different for each payment, but if we use a constant :math:`\beta`, which could be
think about as an approximation that is true when the interest is fixed (as in
our example). Then we have:

.. math::

   O_k = N \cdot (1+\beta)^k \cdot \prod_{i=1}^k \frac{(1+\beta)^{n-i} - 1}{(1+\beta)^{n-i+1} - 1}


And again, using the telescopic property with :math:`a_i = (1+\beta)^{n-i} - 1` then we have:

.. math::

   \begin{aligned}
   O_k &= N \cdot (1+\beta)^k \cdot \frac{(1+\beta)^{n-k} - 1}{(1+\beta)^n - 1}\\
   &=  N \cdot \frac{(1+\beta)^{n} - (1+\beta)^k}{(1+\beta)^n - 1}
   \end{aligned}


As a check we can see that for :math:`k=n` this amount (the outstanding) is
zero, as it must be. And the amortization can be evaluated using the difference
between 2 outstanding amounts:

.. math::
   A_k = O_{k-1} - O_k = N \cdot \frac{(1+\beta)^{k-1} \cdot \beta}{(1+\beta)^n - 1}

As the time the amortization depends on the payment (:math:`k`) we need to compute the percentage of the notional finally paid as interest by hand doing (remember :math:`I_k = \beta_k \cdot O_k`):

.. math::
   TIR = \sum_{k=1}^n \frac{I_k}{N} = \beta \cdot \sum_{k=1}^n \frac{(1+\beta)^n - (1+\beta)^k}{(1 + \beta)^n - 1}

Which, for the figures given in our example, is: **32,853%**. Almost 273 bps
higher than the constant method.

Real world data
---------------

Now I feel trained enough to give my opinion in the debate: buying or renting,
how is it less likely to get ruined?. In my city, Madrid, I have found the
following prices for the purchase and rental of a home:

* Average price per square meter at purchase (last 12 months): 3,718 €/m\ :sup:`2`\ .
* Average price per square meter in the rent (last 12 months): 16'22 €/m\ :sup:`2`\ .

So lets suppose you are getting a house of 85 m\ :sup:`2`\ , if you buy
it **asking for its entire price**, you are going to pay, considering that it
is a second-hand property, around (this is an approximation) 15% of the house
price as taxes, and looking for fixed rate mortgage I have found the average
value of last year MLRI (Mortgage Loan Reference Index) to be 1'768% (this is a
negative interest rate scenario), with this data, considering a 20 years
maturity loan, you are going to pay **for buying** the house:

.. math::

   \text{house price} &= 3718 \cdot 85 = 316,030 \text{ €} \\
   \text{taxes and interests}  &= \text{house price} \cdot (0'15 + 0'1865) = 106,344'10 \text{ €}


With that money, you could rent the same house during:

.. math::

   \frac{106,344'10}{16'22 \cdot 85} = 76'10 \text{ months}


So you can actually rent the same house that you are buying for more than 6
years. You would have paid on average a mortgage fee of 1562'53€ and the rent
would be instead 1378'70€. Both this situations are out of scope for most of us
(people around 30 years) but, if you are thinking about buying, you should know
that you are reducing your savings / investment capacity for the next 20 years
(or more), and paying to the Bank and the Government more than 33% of the house
price for letting you buy it. I consider these results a proper approximation
to the current (2020) scenario.

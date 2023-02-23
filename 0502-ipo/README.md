<h2><a href="https://leetcode.com/problems/ipo/">502. IPO</a></h2><h3>Hard</h3><hr><div><p><code>k</code><code>k</code><font papago-translate="cached" papago-id="17"> distinct projects.</font></p>

<p><font papago-translate="cached" papago-id="18">You are given </font><code>n</code><font papago-translate="cached" papago-id="19"> projects where the </font><code>i<sup>th</sup></code><font papago-translate="cached" papago-id="20"> project has a pure profit </font><code>profits[i]</code><font papago-translate="cached" papago-id="21"> and a minimum capital of </font><code>capital[i]</code><font papago-translate="cached" papago-id="22"> is needed to start it.</font></p>

<p><font papago-translate="cached" papago-id="23">Initially, you have </font><code>w</code><font papago-translate="cached" papago-id="24"> capital. When you finish a project, you will obtain its pure profit and the profit will be added to your total capital.</font></p>

<p> <code>k</code></p>

<p papago-id="27" papago-translate="translated">The answer is guaranteed to fit in a 32-bit signed integer.</p>

<p>&nbsp;</p>
<p><strong class="example" papago-id="28" papago-translate="translated">Example 1:</strong></p>

<pre papago-id="29" papago-translate="cached"><strong papago-id="29-0">Input:</strong> k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]
<strong papago-id="29-2">Output:</strong> 4
<strong papago-id="29-4">Explanation:</strong> Since your initial capital is 0, you can only start the project indexed 0.
After finishing it you will obtain profit 1 and your capital becomes 1.
With capital 1, you can either start the project indexed 1 or the project indexed 2.
Since you can choose at most 2 projects, you need to finish the project indexed 2 to get the maximum capital.
Therefore, output the final maximized capital, which is 0 + 1 + 3 = 4.
</pre>

<p><strong class="example" papago-id="0" papago-translate="translated">Example 2:</strong></p>

<pre papago-id="1" papago-translate="cached"><strong papago-id="1-0">Input:</strong> k = 3, w = 0, profits = [1,2,3], capital = [0,1,2]
<strong papago-id="1-2">Output:</strong> 6
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= w &lt;= 10<sup>9</sup></code></li>
	<li><code>n == profits.length</code></li>
	<li><code>n == capital.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= profits[i] &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= capital[i] &lt;= 10<sup>9</sup></code></li>
</ul>
</div>
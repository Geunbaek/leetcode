<h2><a href="https://leetcode.com/problems/find-good-days-to-rob-the-bank/">2100. Find Good Days to Rob the Bank</a></h2><h3>Medium</h3><hr><div><p><font papago-translate="cached" papago-id="0">You and a gang of thieves are planning on robbing a bank. You are given a <strong papago-id="0-1">0-indexed</strong> integer array </font><code>security</code><font papago-translate="translated" papago-id="1">, where </font><code>security[i]</code><font papago-translate="translated" papago-id="2"> is the number of guards on duty on the </font><code>i<sup>th</sup></code><font papago-translate="translated" papago-id="3"> day. The days are numbered starting from </font><code>0</code><font papago-translate="translated" papago-id="4">. You are also given an integer </font><code>time</code><font papago-translate="translated" papago-id="5">.</font></p>

<p><font papago-translate="translated" papago-id="6">The </font><code>i<sup>th</sup></code><font papago-translate="translated" papago-id="7"> day is a good day to rob the bank if:</font></p>

<ul>
	<li><font papago-translate="translated" papago-id="8">There are at least </font><code>time</code><font papago-translate="translated" papago-id="9"> days before and after the </font><code>i<sup>th</sup></code><font papago-translate="translated" papago-id="10"> day,</font></li>
	<li><font papago-translate="translated" papago-id="11">The number of guards at the bank for the </font><code>time</code><font papago-translate="cached" papago-id="12"> days <strong papago-id="12-1">before</strong></font> <code>i</code><font papago-translate="cached" papago-id="13"> are <strong papago-id="13-1">non-increasing</strong>, and</font></li>
	<li><font papago-translate="translated" papago-id="14">The number of guards at the bank for the </font><code>time</code><font papago-translate="cached" papago-id="15"> days <strong papago-id="15-1">after</strong></font> <code>i</code><font papago-translate="cached" papago-id="16"> are <strong papago-id="16-1">non-decreasing</strong>.</font></li>
</ul>

<p><font papago-translate="translated" papago-id="17">More formally, this means day </font><code>i</code><font papago-translate="translated" papago-id="18"> is a good day to rob the bank if and only if </font><code>security[i - time] &gt;= security[i - time + 1] &gt;= ... &gt;= security[i] &lt;= ... &lt;= security[i + time - 1] &lt;= security[i + time]</code><font papago-translate="translated" papago-id="19">.</font></p>

<p>Return <em>a list of <strong>all</strong> days <strong>(0-indexed) </strong>that are good days to rob the bank</em>.<em> The order that the days are returned in does<strong> </strong><strong>not</strong> matter.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> security = [5,3,3,3,5,6,2], time = 2
<strong>Output:</strong> [2,3]
<strong>Explanation:</strong>
On day 2, we have security[0] &gt;= security[1] &gt;= security[2] &lt;= security[3] &lt;= security[4].
On day 3, we have security[1] &gt;= security[2] &gt;= security[3] &lt;= security[4] &lt;= security[5].
No other days satisfy this condition, so days 2 and 3 are the only good days to rob the bank.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> security = [1,1,1,1,1], time = 0
<strong>Output:</strong> [0,1,2,3,4]
<strong>Explanation:</strong>
Since time equals 0, every day is a good day to rob the bank, so return every day.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre papago-id="11" papago-translate="cached"><strong papago-id="11-0">Input:</strong> security = [1,2,3,4,5,6], time = 2
<strong papago-id="11-2">Output:</strong> []
<strong papago-id="11-4">Explanation:</strong>
No day has 2 days before it that have a non-increasing number of guards.
Thus, no day is a good day to rob the bank, so return an empty list.
</pre>

<p>&nbsp;</p>
<p><strong papago-id="12" papago-translate="translated">Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= security.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= security[i], time &lt;= 10<sup>5</sup></code></li>
</ul>
</div>
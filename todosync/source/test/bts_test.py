import unittest

from todosync.source.bts import parse_bug


class MyTestCase(unittest.TestCase):
    def test_parse_open_not_owned_bug(self):
        html = '''
        <body>
<h1>Debian Bug report logs - 
<a href="mailto:965113@bugs.debian.org">#965113</a><br>
golang-blackfriday: Please update to new upstream version 2.0</h1>
<div class="versiongraph"></div>
<div class="pkginfo">
  <p>Package:
     <a class="submitter" href="pkgreport.cgi?package=golang-blackfriday">golang-blackfriday</a>;
Maintainer for <a href="pkgreport.cgi?package=golang-blackfriday">golang-blackfriday</a> is <a href="pkgreport.cgi?maint=team%2Bpkg-go%40tracker.debian.org">Debian Go Packaging Team &lt;team+pkg-go@tracker.debian.org&gt;</a>; </p>

</div>
<div class="buginfo">
  <p>Reported by: <a href="pkgreport.cgi?submitter=siretart%40tauware.de">Reinhard Tartler &lt;siretart@tauware.de&gt;</a></p>
  <p>Date: Thu, 16 Jul 2020 10:39:02 UTC</p>
<p>Severity: normal</p>
<p></p>
</div>
<p><a href="mailto:965113@bugs.debian.org">Reply</a> or <a href="mailto:965113-subscribe@bugs.debian.org">subscribe</a> to this bug.</p>
<p><a href="javascript:toggle_infmessages();">Toggle useless messages</a></p><div class="msgreceived"><p>View this report as an <a href="bugreport.cgi?bug=965113;mbox=yes">mbox folder</a>, <a href="bugreport.cgi?bug=965113;mbox=yes;mboxstatus=yes">status mbox</a>, <a href="bugreport.cgi?bug=965113;mbox=yes;mboxmaint=yes">maintainer mbox</a></p></div>

<div class="infmessage"><hr><p>
<a name="1"></a>
<!-- request_addr: debian-bugs-dist@lists.debian.org, siretart@tauware.de, debian-go@lists.debian.org, Debian Go Packaging Team &lt;team+pkg-go@tracker.debian.org&gt; -->
<!-- time:1594895944 -->
<strong>Report forwarded</strong>
to <code>debian-bugs-dist@lists.debian.org, siretart@tauware.de, debian-go@lists.debian.org, Debian Go Packaging Team &lt;team+pkg-go@tracker.debian.org&gt;</code>:<br>
<code>Bug#965113</code>; Package <code>golang-blackfriday</code>.
 (Thu, 16 Jul 2020 10:39:04 GMT) (<a href="bugreport.cgi?bug=965113;msg=2">full text</a>, <a href="bugreport.cgi?bug=965113;mbox=yes;msg=2">mbox</a>, <a href="#1">link</a>).</p><p></p></div>

<div class="infmessage"><hr><p>
<a name="3"></a>
<!-- time:1594895944 -->
<strong>Acknowledgement sent</strong>
 (Thu, 16 Jul 2020 10:39:04 GMT) (<a href="bugreport.cgi?bug=965113;msg=4">full text</a>, <a href="bugreport.cgi?bug=965113;mbox=yes;msg=4">mbox</a>, <a href="#3">link</a>).</p><p></p></div>

<hr><p class="msgreceived"><a name="5"></a><a name="msg5"></a><a href="#5">Message #5</a> received at submit@bugs.debian.org (<a href="bugreport.cgi?bug=965113;msg=5">full text</a>, <a href="bugreport.cgi?bug=965113;mbox=yes;msg=5">mbox</a>, <a href="mailto:965113@bugs.debian.org?body=On%20Thu%2C%2016%20Jul%202020%2006%3A34%3A18%20-0400%20Reinhard%20Tartler%20%3Csiretart%40tauware.de%3E%20wrote%3A%0A%3E%20Package%3A%20golang-blackfriday%0A%3E%20Severity%3A%20normal%0A%3E%20Control%3A%20block%20964378%20by%20-1%0A%3E%20%0A%3E%20This%20upgrade%20is%20a%20requirement%20of%20the%20new%20go-md2man%202.0%20upstream%20version%2C%0A%3E%20which%20required%20by%20github.com%2Fspf13%2Fcobra%2C%20which%20in%20turns%20is%20required%0A%3E%20by%20libpod%202.0%2C%20and%20thus%20blocks%20%23964378.%0A%3E%20%0A%3E%20I%27ve%20actually%20already%20updated%20the%20package%20in%20the%20experimental%20branch%20at%0A%3E%20https%3A%2F%2Fsalsa.debian.org%2Fgo-team%2Fpackages%2Fgolang-blackfriday%2F-%2Ftree%2Fdebian%2Fexperimental%0A%3E%20%0A%3E%20And%20did%20a%20test%20rebuild%20of%20all%20packages%20using%20ratt%281%29.%20Here%20is%20the%20executive%20summary%3A%0A%3E%20%0A%3E%202020%2F07%2F15%2020%3A51%3A55%20Build%20results%3A%0A%3E%202020%2F07%2F15%2020%3A51%3A55%20PASSED%3A%20gost%0A%3E%202020%2F07%2F15%2020%3A51%3A55%20PASSED%3A%20golang-github-docker-leadership%0A%3E%202020%2F07%2F15%2020%3A51%3A55%20PASSED%3A%20docker-registry%0A%3E%202020%2F07%2F15%2020%3A51%3A55%20PASSED%3A%20golang-github-appc-docker2aci%0A%3E%202020%2F07%2F15%2020%3A51%3A55%20PASSED%3A%20hcloud-cli%0A%3E%202020%2F07%2F15%2020%3A51%3A55%20PASSED%3A%20badger%0A%3E%202020%2F07%2F15%2020%3A51%3A55%20PASSED%3A%20jp%0A%3E%202020%2F07%2F15%2020%3A51%3A55%20PASSED%3A%20nomad%0A%3E%202020%2F07%2F15%2020%3A51%3A55%20PASSED%3A%20golang-github-aelsabbahy-gonetstat%0A%3E%202020%2F07%2F15%2020%3A51%3A55%20PASSED%3A%20vip-manager%0A%3E%202020%2F07%2F15%2020%3A51%3A55%20PASSED%3A%20golang-github-shurcool-gopherjslib%0A%3E%202020%2F07%2F15%2020%3A51%3A55%20PASSED%3A%20golang-github-docker-go-connections%0A%3E%202020%2F07%2F15%2020%3A51%3A55%20PASSED%3A%20golang-github-tonistiigi-fsutil%0A%3E%202020%2F07%2F15%2020%3A51%3A55%20PASSED%3A%20golang-codegangsta-cli%0A%3E%202020%2F07%2F15%2020%3A51%3A55%20PASSED%3A%20golang-github-openshift-imagebuilder%0A%3E%202020%2F07%2F15%2020%3A51%3A55%20PASSED%3A%20golang-github-opencontainers-runtime-tools%0A%3E%202020%2F07%2F15%2020%3A51%3A55%20PASSED%3A%20mender-cli%0A%3E%202020%2F07%2F15%2020%3A51%3A55%20PASSED%3A%20golang-glide%0A%3E%202020%2F07%2F15%2020%3A51%3A55%20PASSED%3A%20golang-github-gopherjs-gopherjs%0A%3E%202020%2F07%2F15%2020%3A51%3A55%20PASSED%3A%20gosu%0A%3E%202020%2F07%2F15%2020%3A51%3A55%20PASSED%3A%20golang-github-blevesearch-bleve%0A%3E%202020%2F07%2F15%2020%3A51%3A55%20PASSED%3A%20nomad-driver-podman%0A%3E%202020%2F07%2F15%2020%3A51%3A55%20PASSED%3A%20golang-github-containers-storage%0A%3E%202020%2F07%2F15%2020%3A51%3A55%20PASSED%3A%20golang-github-containers-buildah%0A%3E%202020%2F07%2F15%2020%3A51%3A55%20PASSED%3A%20notary%0A%3E%202020%2F07%2F15%2020%3A51%3A55%20PASSED%3A%20golang-github-xordataexchange-crypt%0A%3E%202020%2F07%2F15%2020%3A51%3A55%20PASSED%3A%20cadvisor%0A%3E%202020%2F07%2F15%2020%3A51%3A55%20PASSED%3A%20libpod%0A%3E%202020%2F07%2F15%2020%3A51%3A55%20PASSED%3A%20golang-github-containers-psgo%0A%3E%202020%2F07%2F15%2020%3A51%3A55%20PASSED%3A%20vuls%0A%3E%202020%2F07%2F15%2020%3A51%3A55%20PASSED%3A%20golang-github-samalba-dockerclient%0A%3E%202020%2F07%2F15%2020%3A51%3A55%20PASSED%3A%20nomad-driver-lxc%0A%3E%202020%2F07%2F15%2020%3A51%3A55%20PASSED%3A%20golang-github-fsouza-go-dockerclient%0A%3E%202020%2F07%2F15%2020%3A51%3A55%20PASSED%3A%20golang-github-containers-image%0A%3E%202020%2F07%2F15%2020%3A51%3A55%20PASSED%3A%20git-lfs%0A%3E%202020%2F07%2F15%2020%3A51%3A55%20PASSED%3A%20gobgp%0A%3E%202020%2F07%2F15%2020%3A51%3A55%20PASSED%3A%20golang-github-couchbase-moss%0A%3E%202020%2F07%2F15%2020%3A51%3A55%20PASSED%3A%20golang-github-sylabs-sif%0A%3E%202020%2F07%2F15%2020%3A51%3A55%20PASSED%3A%20docker-libkv%0A%3E%202020%2F07%2F15%2020%3A51%3A55%20PASSED%3A%20golang-github-optiopay-kafka%0A%3E%202020%2F07%2F15%2020%3A51%3A55%20FAILED%3A%20golang-github-spf13-viper%2C%20but%20maybe%20unrelated%20to%20new%20changes%20%28see%20buildlogs_blackfriday%2Fgolang-github-spf13-viper_1.6.1-1%20and%20buildlogs_blackfriday_recheck%2Fgolang-github-spf13-viper_1.6.1-1%29%0A%3E%202020%2F07%2F15%2020%3A51%3A55%20FAILED%3A%20google-cloud-print-connector%2C%20but%20maybe%20unrelated%20to%20new%20changes%20%28see%20buildlogs_blackfriday%2Fgoogle-cloud-print-connector_1.12-1%20and%20buildlogs_blackfriday_recheck%2Fgoogle-cloud-print-connector_1.12-1%29%0A%3E%202020%2F07%2F15%2020%3A51%3A55%20FAILED%3A%20rkt%2C%20but%20maybe%20unrelated%20to%20new%20changes%20%28see%20buildlogs_blackfriday%2Frkt_1.30.0%2Bdfsg1-9%20and%20buildlogs_blackfriday_recheck%2Frkt_1.30.0%2Bdfsg1-9%29%0A%3E%202020%2F07%2F15%2020%3A51%3A55%20FAILED%3A%20hugo%2C%20but%20maybe%20unrelated%20to%20new%20changes%20%28see%20buildlogs_blackfriday%2Fhugo_0.73.0-1%20and%20buildlogs_blackfriday_recheck%2Fhugo_0.73.0-1%29%0A%3E%202020%2F07%2F15%2020%3A51%3A55%20FAILED%3A%20golang-github-shenwei356-bwt%2C%20but%20maybe%20unrelated%20to%20new%20changes%20%28see%20buildlogs_blackfriday%2Fgolang-github-shenwei356-bwt_0.0~git20200418.ae79c98-2%20and%20buildlogs_blackfriday_recheck%2Fgolang-github-shenwei356-bwt_0.0~git20200418.ae79c98-2%29%0A%3E%202020%2F07%2F15%2020%3A51%3A55%20FAILED%3A%20golang-github-shenwei356-util%2C%20but%20maybe%20unrelated%20to%20new%20changes%20%28see%20buildlogs_blackfriday%2Fgolang-github-shenwei356-util_0.0~git20190523.f71ff37-2%20and%20buildlogs_blackfriday_recheck%2Fgolang-github-shenwei356-util_0.0~git20190523.f71ff37-2%29%0A&amp;References=%3C87365rvjdh.fsf%40tauware.de%3E&amp;In-Reply-To=%3C87365rvjdh.fsf%40tauware.de%3E&amp;subject=Re%3A%20golang-blackfriday%3A%20Please%20update%20to%20new%20upstream%20version%202.0">reply</a>):</p>
<div class="headers">
<img src="/cgi-bin/libravatar.cgi?email=siretart%40tauware.de" alt="">
<div class="header"><span class="headerfield">To:</span> Debian Bug Tracking System &lt;submit@bugs.debian.org&gt;</div>
<div class="header"><span class="headerfield">Subject:</span> golang-blackfriday: Please update to new upstream version 2.0</div>
<div class="header"><span class="headerfield">Date:</span> Thu, 16 Jul 2020 06:34:18 -0400</div>
</div>
<pre class="message">Package: golang-blackfriday

This upgrade is a requirement of the new go-md2man 2.0 upstream version,
which required by github.com/spf13/cobra, which in turns is required
by libpod 2.0, and thus blocks #964378.
</pre>
'''
        bug = parse_bug(html)
        self.assertEqual(965113, bug['remote_id'])
        self.assertEqual('https://bugs.debian.org/965113', bug['remote_url'])
        self.assertEqual('golang-blackfriday: Please update to new upstream version 2.0', bug['title'])
        self.assertEqual('', bug['description'])  # todo
        self.assertEqual('todo', bug['status'])
        self.assertEqual('bts', bug['kind'])

    def test_parse_open_owned_bug(self):
        html = '''
        <body>
<h1>Debian Bug report logs - 
<a href="mailto:983842@bugs.debian.org">#983842</a><br>
ITP: srcode -- Tool that help developers to manage their codebase in an effective &amp; productive way.</h1>
<div class="versiongraph"></div>
<div class="pkginfo">
  <p>Package:
     <a class="submitter" href="pkgreport.cgi?package=wnpp">wnpp</a>;
Maintainer for <a href="pkgreport.cgi?package=wnpp">wnpp</a> is <a href="pkgreport.cgi?maint=wnpp%40debian.org">wnpp@debian.org</a>; </p>
</div>
<div class="buginfo">
  <p>Reported by: <a href="pkgreport.cgi?submitter=alois%40micard.lu">Alois Micard &lt;alois@micard.lu&gt;</a></p>
  <p>Date: Tue,  2 Mar 2021 07:57:01 UTC</p>
<p>Owned by: <a href="pkgreport.cgi?owner=alois%40micard.lu">Aloïs Micard &lt;alois@micard.lu&gt;</a></p>
<p>Severity: wishlist</p>
<p></p>
</div>
<p><a href="mailto:983842@bugs.debian.org">Reply</a> or <a href="mailto:983842-subscribe@bugs.debian.org">subscribe</a> to this bug.</p>
<p><a href="javascript:toggle_infmessages();">Toggle useless messages</a></p><div class="msgreceived"><p>View this report as an <a href="bugreport.cgi?bug=983842;mbox=yes">mbox folder</a>, <a href="bugreport.cgi?bug=983842;mbox=yes;mboxstatus=yes">status mbox</a>, <a href="bugreport.cgi?bug=983842;mbox=yes;mboxmaint=yes">maintainer mbox</a></p></div>

<div class="infmessage"><hr><p>
<a name="1"></a>
<!-- request_addr: debian-bugs-dist@lists.debian.org, debian-devel@lists.debian.org, debian-go@lists.debian.org, wnpp@debian.org, Aloïs Micard &lt;alois@micard.lu&gt; -->
<!-- time:1614671823 -->
<strong>Report forwarded</strong>
to <code>debian-bugs-dist@lists.debian.org, debian-devel@lists.debian.org, debian-go@lists.debian.org, wnpp@debian.org, Aloïs Micard &lt;alois@micard.lu&gt;</code>:<br>
<code>Bug#983842</code>; Package <code>wnpp</code>.
 (Tue, 02 Mar 2021 07:57:03 GMT) (<a href="bugreport.cgi?bug=983842;msg=2">full text</a>, <a href="bugreport.cgi?bug=983842;mbox=yes;msg=2">mbox</a>, <a href="#1">link</a>).</p><p></p></div>

<div class="infmessage"><hr><p>
<a name="3"></a>
<!-- request_addr: Alois Micard &lt;alois@micard.lu&gt; -->
<!-- time:1614671824 -->
<strong>Acknowledgement sent</strong>
to <code>Alois Micard &lt;alois@micard.lu&gt;</code>:<br>
New Bug report received and forwarded.  Copy sent to <code>debian-devel@lists.debian.org, debian-go@lists.debian.org, wnpp@debian.org, Aloïs Micard &lt;alois@micard.lu&gt;</code>.
 (Tue, 02 Mar 2021 07:57:04 GMT) (<a href="bugreport.cgi?bug=983842;msg=4">full text</a>, <a href="bugreport.cgi?bug=983842;mbox=yes;msg=4">mbox</a>, <a href="#3">link</a>).</p><p></p></div>

<hr><p class="msgreceived"><a name="5"></a><a name="msg5"></a><a href="#5">Message #5</a> received at submit@bugs.debian.org (<a href="bugreport.cgi?bug=983842;msg=5">full text</a>, <a href="bugreport.cgi?bug=983842;mbox=yes;msg=5">mbox</a>, <a href="mailto:983842@bugs.debian.org?body=On%20Tue%2C%202%20Mar%202021%2008%3A55%3A58%20%2B0100%20Alois%20Micard%20%3Calois%40micard.lu%3E%20wrote%3A%0A%3E%20Package%3A%20wnpp%0A%3E%20Severity%3A%20wishlist%0A%3E%20Owner%3A%20Alo%C3%AFs%20Micard%20%3Calois%40micard.lu%3E%0A%3E%20%0A%3E%20%2A%20Package%20name%20%20%20%20%3A%20srcode%0A%3E%20%20%20Version%20%20%20%20%20%20%20%20%20%3A%200.7.2-1%0A%3E%20%20%20Upstream%20Author%20%3A%20Alo%C3%AFs%20Micard%0A%3E%20%2A%20URL%20%20%20%20%20%20%20%20%20%20%20%20%20%3A%20https%3A%2F%2Fgithub.com%2Fcreekorful%2Fsrcode%0A%3E%20%2A%20License%20%20%20%20%20%20%20%20%20%3A%20GPL-3.0%0A%3E%20%20%20Programming%20Lang%3A%20Go%0A%3E%20%20%20Description%20%20%20%20%20%3A%20Tool%20that%20help%20developers%20to%20manage%20their%20codebase%20in%20an%20effective%20%26%20productive%20way.%0A%3E%20%0A%3E%20%20srcode%20is%20a%20tool%20that%20help%20developers%20to%20manage%20their%20codebase%20in%20an%20effective%0A%3E%20%20%26%20productive%20way.%0A%3E%20%0A%3E%20%20Cheers%21%0A%3E%20%0A%3E%20%0A&amp;References=%3C26d42909-3a30-41af-be56-26beaabce721%40DAG1EX1.emp2.local%3E&amp;In-Reply-To=%3C26d42909-3a30-41af-be56-26beaabce721%40DAG1EX1.emp2.local%3E&amp;subject=Re%3A%20ITP%3A%20srcode%20--%20Tool%20that%20help%20developers%20to%20manage%20their%20codebase%20in%20an%20effective%20%26%20productive%20way.">reply</a>):</p>
<div class="headers">
<img src="/cgi-bin/libravatar.cgi?email=alois%40micard.lu" alt="">
<div class="header"><span class="headerfield">From:</span> Alois Micard &lt;alois@micard.lu&gt;</div>
<div class="header"><span class="headerfield">To:</span> &lt;submit@bugs.debian.org&gt;</div>
<div class="header"><span class="headerfield">Subject:</span> ITP: srcode -- Tool that help developers to manage their codebase in an effective &amp; productive way.</div>
<div class="header"><span class="headerfield">Date:</span> Tue, 2 Mar 2021 08:55:58 +0100</div>
</div>
<pre class="message">Package: wnpp
Severity: wishlist
Owner: Aloïs Micard &lt;alois@micard.lu&gt;

* Package name    : srcode
  Version         : 0.7.2-1
  Upstream Author : Aloïs Micard
* URL             : <a href="https://github.com/creekorful/srcode">https://github.com/creekorful/srcode</a>
* License         : GPL-3.0
  Programming Lang: Go
  Description     : Tool that help developers to manage their codebase in an effective &amp; productive way.

 srcode is a tool that help developers to manage their codebase in an effective
 &amp; productive way.

 Cheers!
</pre>
'''
        bug = parse_bug(html)
        self.assertEqual(983842, bug['remote_id'])
        self.assertEqual('https://bugs.debian.org/983842', bug['remote_url'])
        self.assertEqual(
            'ITP: srcode -- Tool that help developers to manage their codebase in an effective & productive way.',
            bug['title'])
        self.assertEqual('', bug['description'])  # todo
        self.assertEqual('in_progress', bug['status'])
        self.assertEqual('bts', bug['kind'])

    def test_parse_closed_bug(self):
        html = '''
        <body>
<h1>Debian Bug report logs - 
<a href="mailto:889201@bugs.debian.org">#889201</a><br>
O: golang-github-twinj-uuid -- RFC 4122 and DCE 1.1 compliant UUIDs in Go</h1>
<div class="versiongraph"><a href="version.cgi?absolute=0;info=1;collapse=1;fixed=golang-github-twinj-uuid%2F0.10.0%2Bgit20160909.96.7bbe408-6;package=wnpp"><img alt="version graph" src="version.cgi?absolute=0;height=2;collapse=1;fixed=golang-github-twinj-uuid%2F0.10.0%2Bgit20160909.96.7bbe408-6;package=wnpp;width=2"></a></div>
<div class="pkginfo">
  <p>Package:
     <a class="submitter" href="pkgreport.cgi?package=wnpp">wnpp</a>;
Maintainer for <a href="pkgreport.cgi?package=wnpp">wnpp</a> is <a href="pkgreport.cgi?maint=wnpp%40debian.org">wnpp@debian.org</a>; </p>

</div>

<div class="buginfo">
  <p>Date: Sat,  3 Feb 2018 07:21:33 UTC</p>

<p>Severity: normal</p>
<p></p>

<p>Fixed in version golang-github-twinj-uuid/0.10.0+git20160909.96.7bbe408-6</p>

<p><strong>Done:</strong> Aloïs Micard &lt;alois@micard.lu&gt;</p>

</div>

<p><a href="mailto:889201@bugs.debian.org">Reply</a> or <a href="mailto:889201-subscribe@bugs.debian.org">subscribe</a> to this bug.</p>
<p><a href="javascript:toggle_infmessages();">Toggle useless messages</a></p><div class="msgreceived"><p>View this report as an <a href="bugreport.cgi?bug=889201;mbox=yes">mbox folder</a>, <a href="bugreport.cgi?bug=889201;mbox=yes;mboxstatus=yes">status mbox</a>, <a href="bugreport.cgi?bug=889201;mbox=yes;mboxmaint=yes">maintainer mbox</a></p></div>

<div class="infmessage"><hr><p>
<a name="1"></a>
<!-- request_addr: debian-bugs-dist@lists.debian.org, wnpp@debian.org -->
<!-- time:1517642496 -->
<strong>Report forwarded</strong>
to <code>debian-bugs-dist@lists.debian.org, wnpp@debian.org</code>:<br>
<code>Bug#889201</code>; Package <code>wnpp</code>.
 (Sat, 03 Feb 2018 07:21:36 GMT) (<a href="bugreport.cgi?bug=889201;msg=2">full text</a>, <a href="bugreport.cgi?bug=889201;mbox=yes;msg=2">mbox</a>, <a href="#1">link</a>).</p><p></p></div>

<div class="infmessage"><hr><p>
<a name="3"></a>
<!-- time:1517642496 -->
<strong>Acknowledgement sent</strong>
New Bug report received and forwarded.  Copy sent to <code>wnpp@debian.org</code>.
 (Sat, 03 Feb 2018 07:21:36 GMT) (<a href="bugreport.cgi?bug=889201;msg=4">full text</a>, <a href="bugreport.cgi?bug=889201;mbox=yes;msg=4">mbox</a>, <a href="#3">link</a>).</p><p></p></div>

<div class="headers">
<div class="header"><span class="headerfield">To:</span> submit@bugs.debian.org</div>
<div class="header"><span class="headerfield">Subject:</span> O: golang-github-twinj-uuid - RFC 4122 and DCE 1.1 compliant UUIDs
 in Go</div>
<div class="header"><span class="headerfield">Date:</span> Sat, 3 Feb 2018 01:19:19 -0600</div>
</div>
<pre class="message">Package: wnpp
Severity: normal

This package was added to Debian as a dependency of Gitea. I am no longer
working on Gitea and no longer have a reason to continue maintaining the
dependencies.

-- 
</pre>
'''

        bug = parse_bug(html)
        self.assertEqual(889201, bug['remote_id'])
        self.assertEqual('https://bugs.debian.org/889201', bug['remote_url'])
        self.assertEqual('O: golang-github-twinj-uuid -- RFC 4122 and DCE 1.1 compliant UUIDs in Go', bug['title'])
        self.assertEqual('', bug['description'])  # todo
        self.assertEqual('done', bug['status'])
        self.assertEqual('bts', bug['kind'])


if __name__ == '__main__':
    unittest.main()

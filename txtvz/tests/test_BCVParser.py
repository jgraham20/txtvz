
import pytest
from txtvz import BCVParser

class TestBCVParser:

    p = None
    tokens = None

    def setUp(self):
        self.p = BCVParser()

    def test_osis_simple(self):
        p = BCVParser()
        assert p.parse('First John 1:1').osis() == '1JN.1.1'

    def test_osis_continue(self):
        p = BCVParser()
        assert p.parse('Titus 1:1 through 2').osis() == 'Titus.1.1-Titus.1.2'
        assert p.parse('Matt 1through2').osis() == 'Matt.1-Matt.2'
        assert p.parse('Phlm 2 THROUGH 3').osis() == 'Phlm.1.2-Phlm.1.3'
        assert p.parse('Titus 1:1 thru 2').osis() == 'Titus.1.1-Titus.1.2'
        assert p.parse('Matt 1thru2').osis() == 'Matt.1-Matt.2'
        assert p.parse('Phlm 2 THRU 3').osis() == 'Phlm.1.2-Phlm.1.3'
        assert p.parse('Titus 1:1 to 2').osis() == 'Titus.1.1-Titus.1.2'
        assert p.parse('Matt 1to2').osis() == 'Matt.1-Matt.2'
        assert p.parse('Phlm 2 TO 3').osis() == 'Phlm.1.2-Phlm.1.3'

    def test_osis_chapter(self):
        p = BCVParser()
        assert p.parse('Titus 1:1, chapters 2').osis() == 'Titus.1.1,Titus.2'
        assert p.parse('Matt 3:4 CHAPTERS 6').osis() == 'Matt.3.4,Matt.6'
        assert p.parse('Titus 1:1, chapter 2').osis() == 'Titus.1.1,Titus.2'
        assert p.parse('Matt 3:4 CHAPTER 6').osis() == 'Matt.3.4,Matt.6'
        assert p.parse('Titus 1:1, chapts. 2').osis() == 'Titus.1.1,Titus.2'
        assert p.parse('Matt 3:4 CHAPTS. 6').osis() == 'Matt.3.4,Matt.6'
        assert p.parse('Titus 1:1, chapts 2').osis() == 'Titus.1.1,Titus.2'
        assert p.parse('Matt 3:4 CHAPTS 6').osis() == 'Matt.3.4,Matt.6'
        assert p.parse('Titus 1:1, chpts. 2').osis() == 'Titus.1.1,Titus.2'
        assert p.parse('Matt 3:4 CHPTS. 6').osis() == 'Matt.3.4,Matt.6'
        assert p.parse('Titus 1:1, chpts 2').osis() == 'Titus.1.1,Titus.2'
        assert p.parse('Matt 3:4 CHPTS 6').osis() == 'Matt.3.4,Matt.6'
        assert p.parse('Titus 1:1, chapt. 2').osis() == 'Titus.1.1,Titus.2'
        assert p.parse('Matt 3:4 CHAPT. 6').osis() == 'Matt.3.4,Matt.6'
        assert p.parse('Titus 1:1, chapt 2').osis() == 'Titus.1.1,Titus.2'
        assert p.parse('Matt 3:4 CHAPT 6').osis() == 'Matt.3.4,Matt.6'
        assert p.parse('Titus 1:1, chaps. 2').osis() == 'Titus.1.1,Titus.2'
        assert p.parse('Matt 3:4 CHAPS. 6').osis() == 'Matt.3.4,Matt.6'
        assert p.parse('Titus 1:1, chaps 2').osis() == 'Titus.1.1,Titus.2'
        assert p.parse('Matt 3:4 CHAPS 6').osis() == 'Matt.3.4,Matt.6'
        assert p.parse('Titus 1:1, chap. 2').osis() == 'Titus.1.1,Titus.2'
        assert p.parse('Matt 3:4 CHAP. 6').osis() == 'Matt.3.4,Matt.6'
        assert p.parse('Titus 1:1, chap 2').osis() == 'Titus.1.1,Titus.2'
        assert p.parse('Matt 3:4 CHAP 6').osis() == 'Matt.3.4,Matt.6'
        assert p.parse('Titus 1:1, chp. 2').osis() == 'Titus.1.1,Titus.2'
        assert p.parse('Matt 3:4 CHP. 6').osis() == 'Matt.3.4,Matt.6'
        assert p.parse('Titus 1:1, chp 2').osis() == 'Titus.1.1,Titus.2'
        assert p.parse('Matt 3:4 CHP 6').osis() == 'Matt.3.4,Matt.6'
        assert p.parse('Titus 1:1, chs. 2').osis() == 'Titus.1.1,Titus.2'
        assert p.parse('Matt 3:4 CHS. 6').osis() == 'Matt.3.4,Matt.6'
        assert p.parse('Titus 1:1, chs 2').osis() == 'Titus.1.1,Titus.2'
        assert p.parse('Matt 3:4 CHS 6').osis() == 'Matt.3.4,Matt.6'
        assert p.parse('Titus 1:1, cha. 2').osis() == 'Titus.1.1,Titus.2'
        assert p.parse('Matt 3:4 CHA. 6').osis() == 'Matt.3.4,Matt.6'
        assert p.parse('Titus 1:1, cha 2').osis() == 'Titus.1.1,Titus.2'
        assert p.parse('Matt 3:4 CHA 6').osis() == 'Matt.3.4,Matt.6'
        assert p.parse('Titus 1:1, ch. 2').osis() == 'Titus.1.1,Titus.2'
        assert p.parse('Matt 3:4 CH. 6').osis() == 'Matt.3.4,Matt.6'
        assert p.parse('Titus 1:1, ch 2').osis() == 'Titus.1.1,Titus.2'
        assert p.parse('Matt 3:4 CH 6').osis() == 'Matt.3.4,Matt.6'

    def test_osis_verses(self):
        p = BCVParser()
        assert p.parse('Exod 1:1 verses 3').osis() == 'Exod.1.1,Exod.1.3'
        assert p.parse('Phlm VERSES 6').osis() == 'Phlm.1.6'
        assert p.parse('Exod 1:1 verse 3').osis() == 'Exod.1.1,Exod.1.3'
        assert p.parse('Phlm VERSE 6').osis() == 'Phlm.1.6'
        assert p.parse('Exod 1:1 ver. 3').osis() == 'Exod.1.1,Exod.1.3'
        assert p.parse('Phlm VER. 6').osis() == 'Phlm.1.6'
        assert p.parse('Exod 1:1 ver 3').osis() == 'Exod.1.1,Exod.1.3'
        assert p.parse('Phlm VER 6').osis() == 'Phlm.1.6'
        assert p.parse('Exod 1:1 vss. 3').osis() == 'Exod.1.1,Exod.1.3'
        assert p.parse('Phlm VSS. 6').osis() == 'Phlm.1.6'
        assert p.parse('Exod 1:1 vss 3').osis() == 'Exod.1.1,Exod.1.3'
        assert p.parse('Phlm VSS 6').osis() == 'Phlm.1.6'
        assert p.parse('Exod 1:1 vs. 3').osis() == 'Exod.1.1,Exod.1.3'
        assert p.parse('Phlm VS. 6').osis() == 'Phlm.1.6'
        assert p.parse('Exod 1:1 vs 3').osis() == 'Exod.1.1,Exod.1.3'
        assert p.parse('Phlm VS 6').osis() == 'Phlm.1.6'
        assert p.parse('Exod 1:1 vv. 3').osis() == 'Exod.1.1,Exod.1.3'
        assert p.parse('Phlm VV. 6').osis() == 'Phlm.1.6'
        assert p.parse('Exod 1:1 vv 3').osis() == 'Exod.1.1,Exod.1.3'
        assert p.parse('Phlm VV 6').osis() == 'Phlm.1.6'
        assert p.parse('Exod 1:1 v. 3').osis() == 'Exod.1.1,Exod.1.3'
        assert p.parse('Phlm V. 6').osis() == 'Phlm.1.6'
        assert p.parse('Exod 1:1 v 3').osis() == 'Exod.1.1,Exod.1.3'
        assert p.parse('Phlm V 6').osis() == 'Phlm.1.6'

    def test_osis_additional(self):
        p = BCVParser()
        assert p.parse('Exod 1:1 and 3').osis() == 'Exod.1.1,Exod.1.3'
        assert p.parse('Phlm 2 AND 6').osis() == 'Phlm.1.2,Phlm.1.6'
        assert p.parse('Exod 1:1 compare 3').osis() == 'Exod.1.1,Exod.1.3'
        assert p.parse('Phlm 2 COMPARE 6').osis() == 'Phlm.1.2,Phlm.1.6'
        assert p.parse('Exod 1:1 cf. 3').osis() == 'Exod.1.1,Exod.1.3'
        assert p.parse('Phlm 2 CF. 6').osis() == 'Phlm.1.2,Phlm.1.6'
        assert p.parse('Exod 1:1 cf 3').osis() == 'Exod.1.1,Exod.1.3'
        assert p.parse('Phlm 2 CF 6').osis() == 'Phlm.1.2,Phlm.1.6'
        assert p.parse('Exod 1:1 see also 3').osis() == 'Exod.1.1,Exod.1.3'
        assert p.parse('Phlm 2 SEE ALSO 6').osis() == 'Phlm.1.2,Phlm.1.6'
        assert p.parse('Exod 1:1 also 3').osis() == 'Exod.1.1,Exod.1.3'
        assert p.parse('Phlm 2 ALSO 6').osis() == 'Phlm.1.2,Phlm.1.6'
        assert p.parse('Exod 1:1 see 3').osis() == 'Exod.1.1,Exod.1.3'
        assert p.parse('Phlm 2 SEE 6').osis() == 'Phlm.1.2,Phlm.1.6'

    def test_osis_title(self):
        p = BCVParser()
        assert p.parse('Ps 3 title, 4:2, 5:title').osis() == 'Ps.3.1,Ps.4.2,Ps.5.1'
        assert p.parse('PS 3 TITLE, 4:2, 5:TITLE').osis() == 'Ps.3.1,Ps.4.2,Ps.5.1'

    def test_osis_ff(self):
        p = BCVParser()
        assert p.parse('Rev 3ff, 4:2ff').osis() == 'Rev.3-Rev.22,Rev.4.2-Rev.4.11'
        assert p.parse('REV 3 FF, 4:2 FF').osis() == 'Rev.3-Rev.22,Rev.4.2-Rev.4.11'
        assert p.parse('Rev 3f, 4:2f').osis() == 'Rev.3-Rev.22,Rev.4.2-Rev.4.11'
        assert p.parse('REV 3 F, 4:2 F').osis() == 'Rev.3-Rev.22,Rev.4.2-Rev.4.11'

    def test_osis_and_trans(self):
        p = BCVParser()
        pass
        # assert p.parse('Lev 1 (AMP)').osis_and_translations(), [['Lev.1', 'AMP']]
        # assert p.parse('lev 1 amp').osis_and_translations(), [['Lev.1', 'AMP']]
        # assert p.parse('Lev 1 (ASV)').osis_and_translations(), [['Lev.1', 'ASV']]
        # assert p.parse('lev 1 asv').osis_and_translations(), [['Lev.1', 'ASV']]
        # assert p.parse('Lev 1 (CEB)').osis_and_translations(), [['Lev.1', 'CEB']]
        # assert p.parse('lev 1 ceb').osis_and_translations(), [['Lev.1', 'CEB']]
        # assert p.parse('Lev 1 (CEV)').osis_and_translations(), [['Lev.1', 'CEV']]
        # assert p.parse('lev 1 cev').osis_and_translations(), [['Lev.1', 'CEV']]
        # assert p.parse('Lev 1 (ERV)').osis_and_translations(), [['Lev.1', 'ERV']]
        # assert p.parse('lev 1 erv').osis_and_translations(), [['Lev.1', 'ERV']]
        # assert p.parse('Lev 1 (ESV)').osis_and_translations(), [['Lev.1', 'ESV']]
        # assert p.parse('lev 1 esv').osis_and_translations(), [['Lev.1', 'ESV']]
        # assert p.parse('Lev 1 (HCSB)').osis_and_translations(), [['Lev.1', 'HCSB']]
        # assert p.parse('lev 1 hcsb').osis_and_translations(), [['Lev.1', 'HCSB']]
        # assert p.parse('Lev 1 (KJV)').osis_and_translations(), [['Lev.1', 'KJV']]
        # assert p.parse('lev 1 kjv').osis_and_translations(), [['Lev.1', 'KJV']]
        # assert p.parse('Lev 1 (LXX)').osis_and_translations(), [['Lev.1', 'LXX']]
        # assert p.parse('lev 1 lxx').osis_and_translations(), [['Lev.1', 'LXX']]
        # assert p.parse('Lev 1 (MSG)').osis_and_translations(), [['Lev.1', 'MSG']]
        # assert p.parse('lev 1 msg').osis_and_translations(), [['Lev.1', 'MSG']]
        # assert p.parse('Lev 1 (NAB)').osis_and_translations(), [['Lev.1', 'NAB']]
        # assert p.parse('lev 1 nab').osis_and_translations(), [['Lev.1', 'NAB']]
        # assert p.parse('Lev 1 (NABRE)').osis_and_translations(), [['Lev.1', 'NABRE']]
        # assert p.parse('lev 1 nabre').osis_and_translations(), [['Lev.1', 'NABRE']]
        # assert p.parse('Lev 1 (NAS)').osis_and_translations(), [['Lev.1', 'NASB']]
        # assert p.parse('lev 1 nas').osis_and_translations(), [['Lev.1', 'NASB']]
        # assert p.parse('Lev 1 (NASB)').osis_and_translations(), [['Lev.1', 'NASB']]
        # assert p.parse('lev 1 nasb').osis_and_translations(), [['Lev.1', 'NASB']]
        # assert p.parse('Lev 1 (NIRV)').osis_and_translations(), [['Lev.1', 'NIRV']]
        # assert p.parse('lev 1 nirv').osis_and_translations(), [['Lev.1', 'NIRV']]
        # assert p.parse('Lev 1 (NIV)').osis_and_translations(), [['Lev.1', 'NIV']]
        # assert p.parse('lev 1 niv').osis_and_translations(), [['Lev.1', 'NIV']]
        # assert p.parse('Lev 1 (NKJV)').osis_and_translations(), [['Lev.1', 'NKJV']]
        # assert p.parse('lev 1 nkjv').osis_and_translations(), [['Lev.1', 'NKJV']]
        # assert p.parse('Lev 1 (NLT)').osis_and_translations(), [['Lev.1', 'NLT']]
        # assert p.parse('lev 1 nlt').osis_and_translations(), [['Lev.1', 'NLT']]
        # assert p.parse('Lev 1 (NRSV)').osis_and_translations(), [['Lev.1', 'NRSV']]
        # assert p.parse('lev 1 nrsv').osis_and_translations(), [['Lev.1', 'NRSV']]
        # assert p.parse('Lev 1 (RSV)').osis_and_translations(), [['Lev.1', 'RSV']]
        # assert p.parse('lev 1 rsv').osis_and_translations(), [['Lev.1', 'RSV']]
        # assert p.parse('Lev 1 (TNIV)').osis_and_translations(), [['Lev.1', 'TNIV']]
        #assert p.parse('lev 1 tniv').osis_and_translations(), [['Lev.1', 'TNIV']]

    def test_osis_multiple_books(self):
        p = BCVParser()
        assert p.parse('1st through 3rd  Jh').osis() == '1John.1-3John.1'
        assert p.parse('1st thru 3rd  Jh').osis() == '1John.1-3John.1'
        assert p.parse('1st to 3rd  Jh').osis() == '1John.1-3John.1'
        assert p.parse('1st through 3rd  Jn').osis() == '1John.1-3John.1'
        assert p.parse('1st thru 3rd  Jn').osis() == '1John.1-3John.1'
        assert p.parse('1st to 3rd  Jn').osis() == '1John.1-3John.1'
        assert p.parse('1st through 3rd  Jo').osis() == '1John.1-3John.1'
        assert p.parse('1st thru 3rd  Jo').osis() == '1John.1-3John.1'
        assert p.parse('1st to 3rd  Jo').osis() == '1John.1-3John.1'

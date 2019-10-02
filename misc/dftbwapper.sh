#!/bin/sh
/home/xwang224/crystalspells2/tools/v2dftb.py
rm KPOINTS POTCAR INCAR

/home/xwang224/bin/dftb+ > job.out
echo 0 > OSZICAR

/home/xwang224/crystalspells2/tools/dftb2v.py



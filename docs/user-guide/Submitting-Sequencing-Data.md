<!-- uncomment when generating PDF in Atom 
# Submitting Sequencing Data
-->
<!-- comment out when generating PDF in Atom -->
**[PDF version](https://github.com/informatics-isi-edu/gudmap-rbk/wiki/Submitting-Sequencing-Data.pdf)**


Table of contents:
* [Submitting sequencing data](#submitting-sequencing-data-rna-seq-chip-seq-atac-seq-scrna-seq)
    1. [Join the kidney-writers group](https://github.com/informatics-isi-edu/gudmap-rbk/wiki/Submitting-Sequencing-Data/#1-join-the-kidney-writers-group)
    2. [Review Sequencing Data Model](https://github.com/informatics-isi-edu/gudmap-rbk/wiki/Submitting-Sequencing-Data/#2-sequencing-data-model)
    3. [Create metadata records](https://github.com/informatics-isi-edu/gudmap-rbk/wiki/Submitting-Sequencing-Data/#3-create-metadata-associated-with-bio-samples-and-sequencing-assays-using-data-explorer)
    4. [Upload files](https://github.com/informatics-isi-edu/gudmap-rbk/wiki/Submitting-Sequencing-Data/#4-uploading-sequencing-and-analysis-files)
* [Submission Dashboard](https://github.com/informatics-isi-edu/gudmap-rbk/wiki/Submitting-Sequencing-Data/#data-submission-dashboard)
* [FAQ](https://github.com/informatics-isi-edu/gudmap-rbk/wiki/Submitting-Sequencing-Data/#frequently-asked-questions)

Related Material:
* [Tutorial slides containing screenshots (Sequencing Model V3---latest)](https://docs.google.com/presentation/d/1dHg9LmThF7vXFYcUDmZ1s0IgmRhIT8qHAGnxkue1TCE/edit#slide=id.g3cef0a6f7b_0_412)
* [Tutorial Slides containing screenshots (Sequencing Model 2)](https://docs.google.com/presentation/d/1Ee4seF4fgGMH5OuB_N6npaH_tGfUT7yFKKS64I9vbzE/edit#slide=id.g3cef0a6f7b_0_432). Most content is applicable to the latest model except: 1) Replicates should be used for bulk and single cell RNA, and 2) Single Cell Metrics is attached to Replicate instead of Experiment. 
* [Video of Webinar from 7/11/2018 (1 hour, 5 min), Sequencing Model 2](https://www.youtube.com/watch?v=HiWwYXLWk8Y&feature=youtu.be). Most content is applicable to the latest model except: 1) Replicates should be used for bulk and single cell RNA, and 2) Single Cell Metrics is attached to Replicate instead of Experiment. 

## Updates

The data model has been updated on 02/01/2019 to unify the replicate and bio-sample metadata among the bulk and single cell RNASeq data. Users can use the same process to submit all sequencing type. The main difference is that single cell data will have "Single Cell Metrics" associated with a replicate. This is not the case for bulk RNASeq data. 

## Submitting sequencing data (RNA-Seq, ChIP-Seq, ATAC-Seq, scRNA-seq)

### 1. Join the `kidney-writers` group. 
* Join the [kidney-writers group](https://app.globus.org/groups/af0b4010-5b75-11e6-9575-22000aef184d/about). 
* When you click the [kidney-writers group](https://app.globus.org/groups/af0b4010-5b75-11e6-9575-22000aef184d/about) link, if you have never used Globus before, you will be given various choices for logging in: via existing credentials (your institution, Google, or ORCID ID) or by creating a new Globus ID. We recommend using an existing credential if that is available. If you decide to use a login with an email different from the one we invited you with - Globus may ask you to link the two emails/accounts. 
* For detailed instruction on how to join different GUDMAP/RBK group, visit [Accessing GUDMAP and RBK Resources](https://github.com/informatics-isi-edu/gudmap-rbk/wiki/Accessing-GUDMAP-and-RBK-Resources). If you have _any_ problems, please email [help@rebuildingakidney.org](mailto:help@rebuildingakidney.org).

### 2. Sequencing data model 

![Sequencing Data Model V3](wiki_images/submitting-data/Sequencing_Data_Model_V3.png)

* Green boxes are the records directly related to this assay type.
* Yellow boxes indicate links to other assay types (in this case _Specimen_ and _Antibody_, which have their own metadata requirements).

A **Study** describes high-level objectives and overall design of the experiments. A study contains one or more experiments. An **Experiment** describes the protocols, procedures, and experiment settings done to a set of Replicates. A **Replicate** contains information about bio-samples as well as its biological and technical replicate numbers. For single cell RNA-Seq, a **Single Cell Metrics** summarizing the statistics of a replicate can be attached to a replicate. All the replicate-specific experimental assays such as sequencing files (i.e. fastq, bam), analysis files (e.g. TPM, RPKM) can be uploaded under **File** and attach to the proper replicate. The study-level analysis files can be uploaded to **Analysis Files** associated with a study.    


**Old Data Models**: The sequencing data model was updated to V3 on 02/01/19. Deprecated data models can be found here:
- [Sequencing Data Model V2](https://github.com/informatics-isi-edu/gudmap-rbk/blob/master/wiki_images/submitting-data/sequencing/Sequencing_Data_Model_V2.png)

### 3. Create metadata associated with bio-samples and sequencing assays using data explorer
* [Create **specimens**](https://www.gudmap.org/chaise/recordedit/#2/Gene_Expression:Specimen?pcid=static/wiki) for each biological replicates involved in the study. Fill in the detail in the `Specimen` form. Provide as much information as you can related to your bio-samples. A `Specimen` record is needed for each biological replicate. A specimen record has an `Internal ID` field that you can use to keep track of different samples; this ID might be handy when you choose a `Specimen` to associate with a `Replicate` later. Note that the plus sign at the upper right corner of the `Specimen` record entry page allows you to create many specimen records simultaneously.  [Specimen Data Submission Guide](https://github.com/informatics-isi-edu/gudmap-rbk/wiki/Submitting-Specimen-Data) provides more detail on how to create a proper `Specimen` record.
  * After a specimen is created, make sure that `Anatomical Sources`, `Specimen Allele` and `Specimen Mouse Strain Contributing to Specimens` are added (if applicable) by clicking `Add` on top of the corresponding tables. Section 3.1 under [Specimen Data Submission Guide](https://github.com/informatics-isi-edu/gudmap-rbk/wiki/Submitting-Specimen-Data) provides short cut on how to assign the same Anatomical Source to multiple specimens. 
  * For kidney organoid specimens, specify the age of the organoid (e.g. "Organoid day 10") in the `Chronological Age` field, and the cell line name (e.g. BJFF6) in the Specimen's `Cell Line` field. Please choose "kidney organoid" as well as "hIPSC" or "hESC" as anatomical sources. 
* [Create **studies**](https://www.rebuildingakidney.org/chaise/recordedit/#2/RNASeq:Study). Fill in the detail in the `Study` form. Please make sure to fill in all the mandatory fields including `Summary` and `Overall Design` of the study. Hover over the field names on that left that have dotted lines underneath for description of the fields. Once all the fields are filled in, click submit to create a study.  
* Create **experiments**. On the detail page of the study, click `Add` on top of the `Experiment` table section to add new experiments. If you don't see any table listed on the page, please click `Show All Related Records` at the upper right corner of the page. Fill in the detail of your experiment, then click submit to create an experiment. Note that multiple experiments can be created simultaneously by clicking the plus button at the upper right corner. 
* Create **experiment settings**. On the detail page of the experiment, click `Add` on top of the `Experiment Settings` table section to add the detail related to the data processing. 
* Create **Antibodies**. On the detail page of the experiment, click `Add` on top of the `Antibody` table to add the detail related to the antibodies used for cell isolation in the experiment. 
* Create **replicates**. On the detail page of the experiment, click `Add` on top of the `Replicate` table to add new replicates. While creating a replicate record, you will be asked to assign a `Specimen` to the replicate. Different specimens are needed for different biological replicates. Only technical replicates can have the same specimen record assigned to them.  
  * While selecting a specimen, you can search for the ones that you have created earlier by using the internal IDs or expand the facet panel to refine the search.  If the specimen of interest doesn't exist, you can create a new one by clicking on the plus sign at the upper right corner of the `Specimen` pop-up window. Be sure to provide as much information as you can related to your bio specimen, and ensure that `Anatomical Sources`, `Specimen Allele` and `Specimen Mouse Strain Contributing to Specimens` are added (if applicable). 
* For single cell RNASeq data, create Single Cell Metrics. On the detail page of an single cell RNASeq replicate, click `Add` on top of the `Single Cell Metrics` table to add new entry.

* Notes:
    * Please make sure that all the relevant records are properly created. `Record Status` associated with your record will inform you whether all mandatory records are "Complete".
    * By default, the `Curation Status` associated with individual record is by default set to `In preparation` which allow you to keep refining or editing your records. It will not be released to the public. Once all the records are ready to submit, please change the `Curation Status` to "Submitted". All records that are "Complete" and "Submitted" will be routed to the bio-curator for final review and finally release to the public. Until the `Curation Status` is marked as "Release", the data will not be visible to the public.
    * For convenience of the data submitter, all records (e.g. Replicates, Specimen, Files) associated with an experiment will have the same `Curation Status` as the experiment. Once the experiment is released, all those related records will also be released.
    * Data submitters can control the curation status of a study and experiments within a study; a study that is released can have experiments that are released co-existing with experiments that are not.

### 4. Uploading sequencing and analysis files

According to the consortium, the fastq files and bam files are mandatory. However, data submitters are encouraged to upload corresponding analysis files if they are available.   

For sequencing files, there should be one R1 (and one R2/I1 if appropriate). This constraint is required for our QC analysis. If a data submitter conducts multiple runs which generates multiple sequencing files per replicate, those fastq's should be concatenated prior to upload.  See [FAQ's](https://github.com/informatics-isi-edu/gudmap-rbk/wiki/Submitting-Sequencing-Data/_edit#frequently-asked-questions) for example code to do that. Contact the data hub for further help, if needed.
 
https://github.com/informatics-isi-edu/gudmap-rbk/wiki/Submitting-Sequencing-Data#frequently-asked-questions

There are 2 different ways to upload files to our data repository: 
1. Through the browser GUI. 
  * Replicate-level files: On the `Replicate` detail page, click `Add` on top of the `File` table section to add sequencing and analysis files associated with a specific replicate. Normally, users will need to upload the actual files to the Hub. For sequencing files that are archived in other permanent repositories (e.g. GEO), a URL to get to the archive can be provided. For human-protected sequencing file stored in dbGaP, please provide `dbGaP Accession ID`.   
  * Study-level files: On the `Study` detail page, click `Add` on top of the `Study Analysis File` table section to add new analysis files associated with your study.

2. Through [DERIVA client tools](Uploading-files-via-Deriva-client-tools). This approach is recommended in the case that there are many very large files (e.g. bigger than 5 GB) to upload. You will need to [install the client tool](Uploading-files-via-Deriva-client-tools) on your system and prepare your directory structure.   

#### 4.1. Supported file extensions

Please follow the following file extension convention below. Remember the fastq and bam files are mandatory: 

| Extension | File Type | Description (will appear in file caption) | mandatory |
|---|---|---|---|
| `.R1.fastq.gz` | FastQ | F reads | mandatory |
| `.R2.fastq.gz` | FastQ | R reads | mandatory for Paired-End |
| `.I1.fastq.gz` | FastQ | I1 reads | optional |
| `.bam` | bam | alignment | mandatory |
| `.bed` | bed | positive regions | optional |
| `.bw` | bigWig | visualization track | optional |
| `.tpm.csv`, `.tmp.tsv`, or `.tpm.txt` | csv, tsv, or txt respectively| expression value | optional |
| `.rpkm.csv`, `.rpkm.tsv`, or `.rpkm.txt` | csv, tsv, or txt respectively | expression value | optional |
| `.fpkm.csv`, `.fpkm.tsv`, or `.fpkm.txt` | csv, tsv, or txt respectively| expression value | optional |
| `.ReadsPerGene.csv`, `.ReadsPerGene.tsv`, or `.ReadsPerGene.txt` | csv, tsv, or txt respectively| Reads per gene | optional |

#### 4.2. Preparing your files on disk

The upload tools will use the names of files and directories (folders) to determine what kind of files you're uploading and which data records to attach them to. We support the following conventions:  
* 4.2.1. [Sequencing or analysis files associated with a replicate](https://github.com/informatics-isi-edu/gudmap-rbk/wiki/Submitting-Sequencing-Data/#421-preparing-replicate-level-sequencing-files)
* 4.2.2. [Study analysis files](https://github.com/informatics-isi-edu/gudmap-rbk/wiki/Submitting-Sequencing-Data#422-preparing-study-level-analysis-files)

##### 4.2.1. Preparing replicate-level sequencing files

The layout of folders for sequencing files is:
```
$userid
  \- deriva
    \- Seq
      \- <Study Internal ID>     
        \- <Experiment Internal ID> 
          \- <Biological Replicate Number>_<Technical Replicate Number>_<Custom Text>.R1.fastq.gz
          \- <Biological Replicate Number>_<Technical Replicate Number>_<Custom Text>.R2.fastq.gz
          \- <Biological Replicate Number>_<Technical Replicate Number>_<Custom Text>.bam
          \- <Biological Replicate Number>_<Technical Replicate Number>_<Custom Text>.bed
          \- <Biological Replicate Number>_<Technical Replicate Number>_<Custom Text>.bw
          \- <Biological Replicate Number>_<Technical Replicate Number>_<Custom Text>.txt
            or 
          \- <Replicate RID>_<Custom Text>.R1.fastq.gz
          \- <Replicate RID>_<Custom Text>.R2.fastq.gz
          \- <Replicate RID>_<Custom Text>.bam
          \- <Replicate_RID>_<Custom Text>.bed
          \- <Replicate_RID>_<Custom Text>.bw
          \- <Replicate RID>_<Custom Text>.txt
```
where
  - `deriva` is the name of our software 
  - `Seq` is a subfolder of `deriva`. This indicates that everything within is the sequencing data (e.g. non single-cell and single cell)
  - `<Study Internal ID>` is what is specified in the study metadata e.g. `NPC_stability`
  - `<Experiment Internal ID>` is what is specified in the sample metadata e.g. `mNPC_RNA`
  - `<Biological Replicate Number>` is the biological replicate number associated with the replicate e.g. `1`
  - `<Technical Replicate Number>` is the technical replicate number associated with the replicate e.g. `1`
  - `<Replicate RID>` is the replicate RID e.g. `Q-Y500`
  - `<Custom Text>` is other metadata associated with the file e.g. `sorted`
  - `<File Extension>` is one of the file extensions that we current supported. _File Extension_ tells the system what type of file is being uploaded.

**Example 1:**

If you have a study called "NPC_stability" with experiments "mNPC_RNA" and "mNPC_ATAC", you'd create two folders `deriva/Seq/NPC_stability/mNPC_RNA` and `deriva/Seq/NPC_stability/mNPC_ATAC` (on Windows, the paths would be `deriva\Seq\NPC_stability\mNPC_RNA` and `deriva\Seq\NPC_stability\mNPC_ATAC`). All the sequencing files are then placed into the respective experiment folders. In the example below, we use _Biological Replicate Number_ and _Technical Replicate Number_ to name the files in experiment "mNPC_RNA" and use the Replicate _RID_ to name the files in the experiment "mNPC_ATAC". Both file naming conventions will be accepted by the client tool. See actual examples of metadata and files in [the NPC_stability Study](https://www.gudmap.org/chaise/record/#2/RNASeq:Study/RID=Q-Y4GW). 

```
$userid
  \- deriva
    \- Seq
      \- NPC_stability  
        \- mNPC_RNA 
          \- 1_1.R1.fastq.gz
          \- 1_1.R2.fastq.gz
          \- 1_1_sorted.bed
          \- 1_1_normalized_profile.bw
          \- 1_1.kpm.txt
          \- ...
        \- mNPC_ATAC
          \- Q-Y5CC.R1.fastq.gz
          \- Q-Y5CC.R2.fastq.gz
          \- Q-Y5CC_sorted.bed
          \- Q-Y5CC_normalized_profile.bw
          \- Q-Y5CC.kpm.txt
          \- ...
```

**Example 2:**
If you have a single-cell RNA study called "mouse_SC_RNASeq" with experiments "m1_e11_cortex" and "m2_p0_cortex", you'd create two folders `deriva/scRNASeq/mouse_SC_RNASeq/m1_e11_cortex` and `deriva/scRNASeq/m2_p0_cortex` (on Windows, the paths would be `deriva\scRNASeq\mouse_SC_RNASeq\m1_e11_cortex` and `deriva\scRNASeq\m2_p0_cortex`). All the sequencing files are then placed into the respective experiment folders. In the example below, we use _Biological Replicate Number_ and _Technical Replicate Number_ to name the files in experiment "m1_e11_cortex" and use the Single Cell Metrics _RID_ to name the files in the experiment "m2_p0_cortex". Both file naming conventions will be accepted by the client tool. See actual examples of metadata and files in [the mouse_SC_RNASeq Study](https://www.gudmap.org/chaise/record/#2/RNASeq:Study/RID=Q-Y4GT). 

```
$userid
  \- deriva
    \- Seq
      \- mouse_SC_RNASeq  
        \- m1_e11_cortex 
          \- 1_1.R1.fastq.gz
          \- 1_1.R2.fastq.gz
          \- 1_1_sorted.bed
          \- 1_1_normalized_profile.bw
          \- 1_1.kpm.txt
          \- ...
        \- m2_p0_cortex
          \- Q-Y4HM.R1.fastq.gz
          \- Q-Y4HM.R2.fastq.gz
          \- Q-Y4HM_sorted.bed
          \- Q-Y4HM_normalized_profile.bw
          \- Q-Y4HM.kpm.txt
          \- ...
```

##### 4.2.2. Preparing study-level analysis files

If there are analysis files that are results of combining data from different experiments together, those files can be added to the `Study Analsysis File` table. Follow the following directory layout to upload those files through the Deriva client tools.  

The layout of folders for analysis files to be linked at the Study level is:
```
$userid
  \- deriva
    \- Seq
      \- <Study Internal ID> 
        \- <file 1>
        \- <file 2>
```
where
  - `deriva` is the name of our software 
  - `Seq` is a subfolder of `deriva`. This indicates that everything within is sequencing data
  - `<Study Internal ID>` is what is specified in the study metadata e.g. `mouse_SC_RNASeq`
  - `<file 1>`, `<file 2>` are files that you want to uploaded so they can be linked to the study. 

**Example**: 

If there are analysis files that are results of combining data from different experiments together, those files can be added 

```
$userid
  \- deriva
    \- Seq
      \- mouse_SC_RNASeq  
        \- analysis.xls
        \- cluster.html
```

### 4.3. Install and Run Deriva Client Tools

Follow the directions for [Uploading files via Deriva client tools](https://github.com/informatics-isi-edu/gudmap-rbk/wiki/Uploading-files-via-Deriva-client-tools). The tools expect the file and directory naming conventions described above.  

## Data Submission Dashboard
The [monthly data submission dashboard](https://www.gudmap.org/chaise/recordset/#2/Dashboard:Monthly_Submission_Dashboard) is available on the GUDMAP/RBK data browser. 

![Monthly Submission Dashboard](wiki_images/Dashboard.png)

## Frequently Asked Questions
**Question**: 10X generates fastq files in the form of `*.R1_001.fastq.gz` (e.g. my_single_cell.R1_001.fastq.gz). How do I rename file names in bulk from `*.R1_001.fastq.gz` to `*.R1.fastq.gz`?

_Answer_**: You can run the following command on the shell prompt to rename files in bulk. 
```
# to change *.R1_001.fastq.gz to *.R1.fastq.gz
> for file in *.fastq.gz; do mv -v "$file" $(echo "$file" | sed 's/.R1_001.fastq.gz$/.R1.fastq.gz/'); done
``` 


**Question**: CellRanger software expects the sequencing files to be in the form of `*.R1_001.fastq.gz`. How do I change the file names from `*.R1.fastq.gz` to `*.R1_001.fastq.gz`?

_Answer_: You can run the following command on the shell prompt to rename files in bulk. 
```
# to change *.R1.fastq.gz to *.R1_001.fastq.gz
> for file in *.fastq.gz; do mv -v "$file" $(echo "$file" | sed 's/.R1.fastq.gz$/.R1_001.fastq.gz/'); done
``` 
**Question**: I have multiple sequencing runs per replicate, so I have multiple R1.fastq.gz. How do I combine these?

_Answer_: You can run the following command in the shell prompt to combine R1.fastq.gz files into one.
```
# to combine *.R1.fastq.gz to one R1.fastq.gz
# rename all the the files you want to combine to match <something>.R1.fastq.gz
# this code will combine all files that match that naming convention in that folder... so don't mix replicates
> cat *.R1.fastq.gz > RID_concat.R1.fastq.gz
```
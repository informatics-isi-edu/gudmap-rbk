#!/usr/bin/python

import sys
import json
from deriva.core import ErmrestCatalog, AttrDict, get_credential, DEFAULT_CREDENTIAL_FILE, tag, urlquote, DerivaServer, get_credential, BaseCLI
from deriva.core.ermrest_model import builtin_types, Schema, Table, Column, Key, ForeignKey

# -----------------------------------------------------------------
# the row structure has to be consistent with the model
def load_table_RNASeq_Reference_Genome(catalog):
    pb = catalog.getPathBuilder()
    table = pb.RNASeq.Reference_Genome

    rows =[
        {
            'Name': 'GRCm38.p6.vM22_indev',
            'Reference_Version': 'GRCm38.p6',
            'Annotation_Version': 'GENCODE vM22',
            'Species': 'Mus musculus',
            'Used_Spike_Ins': False,
            'Description': 'This is an **indevelopment** version of a mouse genome',
            'File_URL': 'https://dev.gudmap.org/hatrac/resources/rnaseq/pipeline/reference_genome/6549414ca89a33298f2ff53b0ee88d8a:2QZVTJLCKUN2BYQHBZZTDM6GKU',
            'File_Name': 'GRCm38.p6.vM22_indev.zip',
            'File_Bytes': 4693653723,
            'File_MD5' : '6549414ca89a33298f2ff53b0ee88d8a'
        },
        {
            'Name': 'GRCh38.p12.v31_indev',
            'Reference_Version': 'GRCh38.p12',
            'Annotation_Version': 'GENCODE v31',
            'Species': 'Homo sapiens',
            'Used_Spike_Ins': True,
            'Description':  'This is an **indevelopment** version of a human genome',
            'File_URL': 'https://dev.gudmap.org/hatrac/resources/rnaseq/pipeline/reference_genome/e4068a78671f0e012726660896946e4b:YTAUQINBKDGZQYPFUIHLWAUKDM',
            'File_Name': 'GRCh38.p12.v31_indev.zip',
            'File_Bytes': 5398855132,
            'File_MD5': 'e4068a78671f0e012726660896946e4b'
        }
    ]
            
    table.insert(rows)

# ----------------------------------------------------------------------

# the row structure has to be consistent with the model
def load_table_RNASeq_Workflow(catalog):
    pb = catalog.getPathBuilder()
    table = pb.RNASeq.Workflow

    rows =[
        {
            'Name': 'BICF mRNA Replicate',
            'Version': 'v0.0.4_indev',
            'Commit_Number': 'c114a62915735a05e4469c25bcf4829b0acee619',
            'Workflow_Type': 'mRNA_Replicate_Workflow',
            'Description': '**BETA indev VERSION**',
            'Source_URL': 'https://git.biohpc.swmed.edu/gudmap_rbk/rna-seq/-/tags/0.0.4_indev',
            'DOI': None,
            'Aligner': 'HISAT2',
            'Aligner_Version': '2.1.0',
            'Sequence_Trimming': True,
            'Duplicate_Removal': True
        }
    ]
            
    table.insert(rows)

    
# -- =================================================================================

def main(server_name, catalog_id, credentials):
    server = DerivaServer('https', server_name, credentials)
    catalog = server.connect_ermrest(catalog_id)
    catalog.dcctx['cid'] = "oneoff/data"
    model = catalog.getCatalogModel()

    #load_table_RNASeq_Reference_Genome(catalog)
    load_table_RNASeq_Workflow(catalog)    

# -- --------------------------------------------------------------
# arguments: 
#  --credential-file (optional if authenticated through deriva-auth)
#  -- host
# e.g. python3 row_mutation.py --credential-file ~/.deriva/credential.json --host staging.gudmap.org

if __name__ == '__main__':
    args = BaseCLI("mutate rows", None, 1).parse_cli()
    credentials = get_credential(args.host, args.credential_file)
    main(args.host, 2, credentials)

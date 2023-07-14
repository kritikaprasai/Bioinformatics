from Bio import SeqIO
import os
import pdb
# Set the directory containing the FASTA files
parent_dir = r"enter your folder path here"

# Traverse the directory structure and find all .fasta files
for root, dirs, files in os.walk(parent_dir):
    for file in files:
        if file.endswith(".fasta"):
            # Get the full path to the file
            file_path = os.path.join(root, file)
            
            # Read the sequences from the file using SeqIO
            seq_records = SeqIO.parse(file_path, "fasta")
            
            # Create a new list of SeqRecord objects with updated headers
            new_seq_records = []
            for record in seq_records:
                new_id = os.path.splitext(file)[0] + "_" + record.id
                new_desc = " ".join([os.path.splitext(file)[0], record.description])
                new_record = record.__class__(record.seq, id=new_id, description=new_desc)
                new_seq_records.append(new_record)
            
            # Write the new sequences to a new file
            out_file = os.path.splitext(file_path)[0] + "_new.fasta"
            SeqIO.write(new_seq_records, out_file, "fasta")

############################################## Generating similarity metrics in RBD Sequence ###########################################################################
from Bio import pairwise2
from Bio import SeqIO
from openpyxl import Workbook

# Read sequences and sequence names from the FASTA file
sequences = []
sequence_names = []
seq_data = r"Aligned_RBD_sequence.fasta"
for record in SeqIO.parse(seq_data, "fasta"):
    sequence_names.append(record.id)
    sequences.append(str(record.seq))

# Calculate similarity scores
def calculate_similarity_score(alignment):
    score = 0
    for i in range(len(alignment[0])):
        if alignment[0][i] == alignment[1][i]:
            score += 1
    return score

# Calculate the similarity matrix in percentage
similarity_matrix = []

# Header row with sequence names
similarity_matrix.append([""] + sequence_names)

for i in range(len(sequences)):
    row = [sequence_names[i]]
    for j in range(len(sequences)):
        alignments = pairwise2.align.globalxx(sequences[i], sequences[j])
        alignment = alignments[0]  # Get the first alignment
        score = calculate_similarity_score(alignment)  # Calculate similarity score (as defined earlier)
        length_i = len(sequences[i])
        length_j = len(sequences[j])
        score_percent = (score / max(length_i, length_j)) * 100  # Normalize score to percentage
        row.append(score_percent)
    similarity_matrix.append(row)

# Print the similarity matrix
for row in similarity_matrix:
    print("\t".join(map(str, row)))

# Write the similarity matrix to an Excel file
wb = Workbook()
ws = wb.active

# Write the data to the worksheet
for row in similarity_matrix:
    ws.append(row)

# Save the workbook to a file
wb.save(r".\similarity_matrix_RBD.xlsx")



# # Calculate the similarity matrix in percentage
# similarity_matrix = []
# for i in range(len(sequences)):
#     scores = []
#     for j in range(len(sequences)):
#         alignments = pairwise2.align.globalxx(sequences[i], sequences[j])
#         alignment = alignments[0]  # Get the first alignment
#         score = calculate_similarity_score(alignment)  # Calculate similarity score (as defined earlier)
#         length_i = len(sequences[i])
#         length_j = len(sequences[j])
#         score_percent = (score / max(length_i, length_j)) * 100  # Normalize score to percentage
#         scores.append(score_percent)
#     similarity_matrix.append(scores)

# # Print the similarity matrix
# for row in similarity_matrix:
#     print(row)

import pandas as pd
from pathlib import Path

categories = ["DNA", "LINE", "LTR", "Other", "Unknown"]
organism_types = ["amphibian", "flatworm"]

threshold = 0.7

data = []
for organism_type in organism_types:
    organism_type_dir = Path(organism_type.lower() + "s")
    species_dirs = [x for x in organism_type_dir.iterdir() if x.is_dir()]
    for directory in species_dirs:
        df = pd.read_csv(directory / f"{directory.name}.csv")

        exclude_columns = ['file', 'accession', 'prediction', 'probability', 'original_id', 'original_classification', 'description']
        filtered_columns = [col for col in df.columns if col not in exclude_columns and '/' not in col]
        df["prediction"] = df[filtered_columns].idxmax(axis=1)
        df["probability"] = df[filtered_columns].max(axis=1)


        df["original_classification"] = df["original_classification"].str.split("/").str[0]
        df.loc[ df["probability"] < threshold, "prediction"] = "Unknown"    

        df.loc[ ~df["prediction"].isin(categories), "prediction"] = "Other"
        df["repeatmodeler_order"] = df["original_classification"].str.split("/").str[0]
        df.loc[ ~df["repeatmodeler_order"].isin(categories), "repeatmodeler_order"] = "Other"
        
        summary_row = {
            'Species': directory.name.replace("_", " "),
            'Total': len(df),
            'Organism Type': organism_type.capitalize(),
        }

        summary_row.update({f"Terrier {k}": v for k, v in df['prediction'].value_counts().to_dict().items()})
        summary_row.update({f"RepeatModeler {k}": v for k, v in df['original_classification'].value_counts().to_dict().items()})

        
        data.append(summary_row)

summary_df = pd.DataFrame(data)
summary_df.sort_values(["Organism Type","Total"], inplace=True, ascending=[True,False])
summary_df.to_csv("summary.csv", index=False)

repeatmodeler_unknown_proportion = summary_df["RepeatModeler Unknown"].sum()/summary_df["Total"].sum()
print(f"RepeatModeler Unknown proportion: {1-repeatmodeler_unknown_proportion:.1%}")

terrier_unknown_proportion = summary_df["Terrier Unknown"].sum()/summary_df["Total"].sum()
print(f"Terrier Unknown proportion: {terrier_unknown_proportion:.1%}")


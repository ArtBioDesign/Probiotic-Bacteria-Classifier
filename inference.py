# cli_inference.py
import argparse
import pandas as pd
import joblib
import os

def main(input_file, output_file):
    df = pd.read_csv(input_file)
    categorical_features = ['Form/Shape', 'colony Color', 'Colony margin', 'Gram’s Staining', 'Cell shape']
    df_onehot = df[categorical_features].astype(str)
    X = pd.get_dummies(df_onehot, prefix=categorical_features, drop_first=False)
    
    automl_loaded = joblib.load('model/autosklearn_model.pkl')
    df['label'] = automl_loaded.predict(X)

    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    df.to_csv(output_file, index=False)
    print(f"✅ 结果已保存至: {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="输入 CSV 文件路径")
    parser.add_argument("-o", "--output", default="Result.csv", help="输出文件路径")
    args = parser.parse_args()
    main(args.input, args.output)



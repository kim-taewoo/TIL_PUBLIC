import fs from 'fs';

export class CsvFileReader {
  data: string[][] = [];

  constructor(public filename: string) {}

  read(): void {
    // encoding 을 명시하지 않으면 string 이 아닌 buffer 를 반환한다. 따라서 encoding 을 명시해서 string 으로 받자.
    this.data = fs
      .readFileSync(this.filename, {
        encoding: 'utf-8',
      })
      .split('\n')
      .map((row: string): string[] => {
        return row.split(',');
      });
  }
}

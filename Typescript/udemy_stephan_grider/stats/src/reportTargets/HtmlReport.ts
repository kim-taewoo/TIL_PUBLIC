import fs from 'fs'

import { OutputTarget } from '../Summary';

export class HtmlReport implements OutputTarget {
  print(report: string): void {
    const html = `
      <div>
        <h1>분석 결과</h1>
        <div>${report}</div>
      </div>
    `;

    fs.writeFileSync('report.html', html);
  }
}

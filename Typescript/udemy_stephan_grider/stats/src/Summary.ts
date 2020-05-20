import { MatchData } from './MatchData';
import { WinsAnalysis } from './analyzers/WinsAnalysis';
import { HtmlReport } from './reportTargets/HtmlReport';

export interface Analyzer {
  run(matches: MatchData[]): string;
}

export interface OutputTarget {
  print(report: string): void;
}

// 이 Summary 클래스는 본인이 어떤 작업을 수행하지 않고, 모두 다른 곳에 delegate(위임) 해서
// 경우에 따라 일들을 해결한다.
export class Summary {
  static winsAnalysisWithHtmlReport(team: string): Summary {
    return new Summary(new WinsAnalysis(team), new HtmlReport());
  }

  constructor(public analyzer: Analyzer, public outputTarget: OutputTarget) {}

  buildAndPrintReport(matches: MatchData[]): void {
    const output = this.analyzer.run(matches);
    this.outputTarget.print(output);
  }
}

"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
var fs_1 = __importDefault(require("fs"));
var HtmlReport = /** @class */ (function () {
    function HtmlReport() {
    }
    HtmlReport.prototype.print = function (report) {
        var html = "\n      <div>\n        <h1>\uBD84\uC11D \uACB0\uACFC</h1>\n        <div>" + report + "</div>\n      </div>\n    ";
        fs_1.default.writeFileSync('report.html', html);
    };
    return HtmlReport;
}());
exports.HtmlReport = HtmlReport;

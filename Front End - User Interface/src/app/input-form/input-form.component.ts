import { Component } from '@angular/core';
import { FileUploadService } from '../file-upload.service';

@Component({
  selector: 'app-input-form',
  templateUrl: './input-form.component.html',
  styleUrls: ['./input-form.component.css']
})
export class InputFormComponent {
  constructor(private fileUploadService: FileUploadService) {}

  onFileSelected(event: any): void {
    const file: File = event.target.files[0];
    this.fileUploadService.uploadFile(file).subscribe(result => {
      // Handle result from backend
      console.log(result);
    });
  }
}

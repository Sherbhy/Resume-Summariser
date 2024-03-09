import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { InputFormComponent } from './input-form/input-form.component'; // Import your InputFormComponent

const routes: Routes = [
  { path: 'input-form', component: InputFormComponent } // Define a route for InputFormComponent
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }

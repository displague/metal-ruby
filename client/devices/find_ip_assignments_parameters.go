// Code generated by go-swagger; DO NOT EDIT.

package devices

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the swagger generate command

import (
	"context"
	"net/http"
	"time"

	"github.com/go-openapi/errors"
	"github.com/go-openapi/runtime"
	cr "github.com/go-openapi/runtime/client"
	"github.com/go-openapi/strfmt"
)

// NewFindIPAssignmentsParams creates a new FindIPAssignmentsParams object
// with the default values initialized.
func NewFindIPAssignmentsParams() *FindIPAssignmentsParams {
	var ()
	return &FindIPAssignmentsParams{

		timeout: cr.DefaultTimeout,
	}
}

// NewFindIPAssignmentsParamsWithTimeout creates a new FindIPAssignmentsParams object
// with the default values initialized, and the ability to set a timeout on a request
func NewFindIPAssignmentsParamsWithTimeout(timeout time.Duration) *FindIPAssignmentsParams {
	var ()
	return &FindIPAssignmentsParams{

		timeout: timeout,
	}
}

// NewFindIPAssignmentsParamsWithContext creates a new FindIPAssignmentsParams object
// with the default values initialized, and the ability to set a context for a request
func NewFindIPAssignmentsParamsWithContext(ctx context.Context) *FindIPAssignmentsParams {
	var ()
	return &FindIPAssignmentsParams{

		Context: ctx,
	}
}

// NewFindIPAssignmentsParamsWithHTTPClient creates a new FindIPAssignmentsParams object
// with the default values initialized, and the ability to set a custom HTTPClient for a request
func NewFindIPAssignmentsParamsWithHTTPClient(client *http.Client) *FindIPAssignmentsParams {
	var ()
	return &FindIPAssignmentsParams{
		HTTPClient: client,
	}
}

/*FindIPAssignmentsParams contains all the parameters to send to the API endpoint
for the find IP assignments operation typically these are written to a http.Request
*/
type FindIPAssignmentsParams struct {

	/*ID
	  Device UUID

	*/
	ID strfmt.UUID
	/*Include
	  related attributes to include

	*/
	Include *string

	timeout    time.Duration
	Context    context.Context
	HTTPClient *http.Client
}

// WithTimeout adds the timeout to the find IP assignments params
func (o *FindIPAssignmentsParams) WithTimeout(timeout time.Duration) *FindIPAssignmentsParams {
	o.SetTimeout(timeout)
	return o
}

// SetTimeout adds the timeout to the find IP assignments params
func (o *FindIPAssignmentsParams) SetTimeout(timeout time.Duration) {
	o.timeout = timeout
}

// WithContext adds the context to the find IP assignments params
func (o *FindIPAssignmentsParams) WithContext(ctx context.Context) *FindIPAssignmentsParams {
	o.SetContext(ctx)
	return o
}

// SetContext adds the context to the find IP assignments params
func (o *FindIPAssignmentsParams) SetContext(ctx context.Context) {
	o.Context = ctx
}

// WithHTTPClient adds the HTTPClient to the find IP assignments params
func (o *FindIPAssignmentsParams) WithHTTPClient(client *http.Client) *FindIPAssignmentsParams {
	o.SetHTTPClient(client)
	return o
}

// SetHTTPClient adds the HTTPClient to the find IP assignments params
func (o *FindIPAssignmentsParams) SetHTTPClient(client *http.Client) {
	o.HTTPClient = client
}

// WithID adds the id to the find IP assignments params
func (o *FindIPAssignmentsParams) WithID(id strfmt.UUID) *FindIPAssignmentsParams {
	o.SetID(id)
	return o
}

// SetID adds the id to the find IP assignments params
func (o *FindIPAssignmentsParams) SetID(id strfmt.UUID) {
	o.ID = id
}

// WithInclude adds the include to the find IP assignments params
func (o *FindIPAssignmentsParams) WithInclude(include *string) *FindIPAssignmentsParams {
	o.SetInclude(include)
	return o
}

// SetInclude adds the include to the find IP assignments params
func (o *FindIPAssignmentsParams) SetInclude(include *string) {
	o.Include = include
}

// WriteToRequest writes these params to a swagger request
func (o *FindIPAssignmentsParams) WriteToRequest(r runtime.ClientRequest, reg strfmt.Registry) error {

	if err := r.SetTimeout(o.timeout); err != nil {
		return err
	}
	var res []error

	// path param id
	if err := r.SetPathParam("id", o.ID.String()); err != nil {
		return err
	}

	if o.Include != nil {

		// query param include
		var qrInclude string
		if o.Include != nil {
			qrInclude = *o.Include
		}
		qInclude := qrInclude
		if qInclude != "" {
			if err := r.SetQueryParam("include", qInclude); err != nil {
				return err
			}
		}

	}

	if len(res) > 0 {
		return errors.CompositeValidationError(res...)
	}
	return nil
}